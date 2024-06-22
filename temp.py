import re

# Read the UTF-8 encoded text from a file
with open('chats/text/WhatsApp Chat with Anuu.txt', 'r', encoding='utf-8') as file:
    log = file.read()

# Define the regular expression pattern to match timestamps and sender names
pattern = r'^(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - (.+)$'


# Function to process the log and combine multiline messages into single lines
def combine_messages(log):
    lines = log.split('\n')
    combined_log = []
    current_message = ''

    for line in lines:
        line = line.strip()
        match = re.match(pattern, line)

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

    return '\n'.join(combined_log)


# Process the log to combine multiline messages into single lines
single_line_log = combine_messages(log)

# Write the processed log back to the file
with open('chats/text/WhatsApp Chat with Anuu.txt', 'w', encoding='utf-8') as file:
    file.write(single_line_log)

print("The file has been updated with the messages set in single lines.")
