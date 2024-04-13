import csv
import re

# Define the regular expression pattern to extract timestamp, sender, and message
pattern = r'(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - ([^:]+): (.*)'

# Open the input text file and create a CSV file for writing
with open('chats/text/WhatsApp Chat with Chitransh.txt', 'r', encoding='utf-8') as input_file, \
        open('chats/csv/WhatsApp Chat with Chitransh.csv', 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer object
    csv_writer = csv.writer(output_file)

    # Write the header row
    csv_writer.writerow(['timestamp', 'sender', 'message'])

    # Iterate through each line in the input text file
    for line in input_file:
        # Attempt to match the pattern in the line
        match = re.match(pattern, line.strip())

        # If a valid match is found
        if match:
            # Extract timestamp, sender, and message from the match groups
            timestamp = match.group(1)
            sender = match.group(2)
            message = match.group(3)

            # Write the extracted data into the CSV file
            csv_writer.writerow([timestamp, sender, message])
