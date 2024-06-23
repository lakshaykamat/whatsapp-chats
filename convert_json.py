import re
import json
from collections import defaultdict
from datetime import datetime

# Define the regular expression patterns
patterns = {
    'timestamp': r'(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - ([^:]+):',
    'message': r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - [^:]+: (.*)',
    'sender': r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - ([^:]+):'
}


def check_date_format(date_str):
    """
    Check the format of the given date string and return the matching format.
    """
    # List of date formats to check against
    date_formats = [
        "%m/%d/%y",  # MM/DD/YY
        "%d/%m/%y",  # DD/MM/YY
        "%y/%m/%d",  # YY/MM/DD
        "%y/%d/%m"  # YY/DD/MM
    ]

    # Try parsing the date string with each format
    for fmt in date_formats:
        try:
            datetime.strptime(date_str, fmt)
            return fmt
        except ValueError:
            continue

    return "Unknown date format"


def count_date_formats(date_strings):
    """
    Count the occurrences of each date format in the list of date strings.
    """

    date_formats = [
        "%m/%d/%y",  # MM/DD/YY
        "%d/%m/%y",  # DD/MM/YY
        "%y/%m/%d",  # YY/MM/DD
        "%y/%d/%m"  # YY/DD/MM
    ]
    date_format_counts = defaultdict(int)

    for date_str in date_strings:
        # Extract the date part before the comma
        date_part = date_str.split(",")[0]
        matched_format = check_date_format(date_part)

        # Increment the count for the matched format
        if matched_format in date_formats:
            date_format_counts[matched_format] += 1
        else:
            date_format_counts["Unknown date format"] += 1

    return date_format_counts


def parse_chat_line(chat_line):
    """
    Parse a single chat line and extract timestamp, sender, and message.

    Args:
    chat_line (str): A single line from the chat.

    Returns:
    dict: A dictionary containing timestamp, sender, and message.
    """
    match_timestamp = re.match(patterns['timestamp'], chat_line)
    match_message = re.match(patterns['message'], chat_line)
    match_sender = re.match(patterns['sender'], chat_line)

    if match_timestamp and match_message:
        timestamp = match_timestamp.group(1)
        sender = match_sender.group(1)
        message = match_message.group(1)
        return {"timestamp": timestamp, "sender": sender, "message": message}
    else:
        mess = chat_line.split("-")
        return {"timestamp": mess[0], "sender": "WhatsApp", "message": mess[1]}


def extract_chat_data(input_file):
    """
    Extract chat data from a text file.

    Args:
    input_file (str): The path to the input text file.

    Returns:
    list: A list of dictionaries containing chat data.
    """
    chat_data = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            parsed_line = parse_chat_line(line.strip())
            if parsed_line:
                chat_data.append(parsed_line)

    return chat_data


def convert_textchat_to_json(input_file, output_file):
    """
    Write chat data to a JSON file.

    Args:
    chat_data (list): A list of dictionaries containing chat data.
    output_file (str): The path to the output JSON file.
    """
    chat_data = extract_chat_data(input_file)
    with open(output_file, "w") as json_file:
        json.dump(chat_data, json_file, indent=4)
    print(f"Chat data has been extracted and written to '{output_file}' file.")
