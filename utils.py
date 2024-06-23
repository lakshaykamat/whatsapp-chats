import re
from datetime import datetime


def read_file(file_path):
    """
    Read the content of a file.

    Args:
    file_path (str): The path to the file.

    Returns:
    str: The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    """
    Write content to a file.

    Args:
    file_path (str): The path to the file.
    content (str): The content to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def combine_messages(log):
    """
    Combine multiline messages into single lines.

    Args:
    log (str): The chat log as a single string.

    Returns:
    str: The processed chat log with each message on a single line.
    """
    # Define a list of regular expression patterns to match timestamps and sender names
    patterns = [
        r'^(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}) - (.+):',
        r'^(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}) - (.+)$'
    ]

    lines = log.split('\n')
    combined_log = []
    current_message = ''
    pattern = None

    for line in lines:
        line = line.strip()
        # Check if the line matches any of the patterns
        for pat in patterns:
            match = re.match(pat, line)
            if match:
                pattern = pat
                break

        if match:
            # If there's a current message, append it to combined_log
            if current_message:
                combined_log.append(current_message.strip())
            # Start a new current message with the matched line
            current_message = line
        else:
            # Append to the current message if it's not a timestamp line
            current_message += ' ' + line.strip()

    # Append the last message if it exists
    if current_message:
        combined_log.append(current_message.strip())

    # Join all messages into a single string with newlines separating each message
    return '\n'.join(combined_log)


def process_whatsapp_log(file_path):
    """
    Process a WhatsApp chat log to combine multiline messages into single lines.

    Args:
    file_path (str): The path to the WhatsApp chat log file.
    """
    log = read_file(file_path)
    single_line_log = combine_messages(log)

    chat_list = single_line_log.split("\n")
    date_formats = count_date_formats(chat_list)
    date_format = max(date_formats, key=date_formats.get)
    print(date_format)
    updated_list = []
    for chat in chat_list:
        time = chat.split(",")[0]
        if date_format != "%m/%d/%y":
            date_obj = datetime.strptime(time, date_format)
            formatted_date = date_obj.strftime("%m/%d/%y")
            time = formatted_date

        updated_list.append(f"{time}, {chat.split(",")[1]}")
    # print(type(single_line_log))
    write_file("text.txt", single_line_log)
    print("The file has been updated with the messages set in single lines.")


def format_time_in_chat(chat_list):
    updated_list = []
    date_formats = count_date_formats(chat_list)
    date_format = max(date_formats, key=date_formats.get)
    for chat in chat_list:
        time = chat.split(",")[0]
        date_obj = datetime.strptime(time, date_format)
        formatted_date = date_obj.strftime("%m/%d/%y")
        updated_list.append(f"{formatted_date}, {chat.split(",")[1]}")
    return updated_list
