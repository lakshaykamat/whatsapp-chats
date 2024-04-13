import re
import json

# Define the regular expression patterns
timestamp_pattern = r'(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - ([^:]+):'
message_pattern = r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - [^:]+: (.*)'

def parse_chat_line(chat_line):
    """
    Parse a single chat line and extract timestamp, sender, and message.

    Args:
    chat_line (str): A single line from the chat.

    Returns:
    dict: A dictionary containing timestamp, sender, and message.
    """
    match_timestamp = re.match(timestamp_pattern, chat_line)
    match_message = re.match(message_pattern, chat_line)
    if match_timestamp and match_message:
        timestamp = match_timestamp.group(1)
        sender = match_timestamp.group(2)
        message = match_message.group(1)
        return {"timestamp": timestamp, "sender": sender, "message": message}
    else:
        return None

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
            parsed_line = parse_chat_line(line)
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

