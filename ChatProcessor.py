from datetime import datetime
import re

class ChatProcessor:
    def __init__(self, chat_file):
        self.time_gap = None
        self.chat_file = chat_file
        self.sender_message_count = {}
        self.sender_names = set()

    def process_chat_file(self):
        """
        Process the chat file to count messages from each sender and get sender names.
        """
        # Define a regular expression pattern to match the sender's name
        pattern = r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - ([^:]+):'

        # Process the chat file
        with open(self.chat_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            first_message_time = self.extract_time(lines[0])
            last_message_time = self.extract_time(lines[-1])
            self.time_gap = self.calculate_time_difference(first_message_time, last_message_time)

            for line in lines:
                match = re.match(pattern, line)
                if match:
                    sender = match.group(1)
                    self.sender_names.add(sender)
                    self.sender_message_count[sender] = self.sender_message_count.get(sender, 0) + 1

    def calculate_time_difference(self, start_time, end_time):
        """
        Calculate the time difference between two timestamps.

        Args:
        start_time (str): The start timestamp in the format "YY/MM/DD".
        end_time (str): The end timestamp in the format "YY/MM/DD".

        Returns:
        timedelta: The time difference between the two timestamps.
        """
        # Convert the timestamps to datetime objects
        start_datetime = datetime.strptime(start_time, "%y/%m/%d")
        end_datetime = datetime.strptime(end_time, "%y/%m/%d")

        # Calculate the time difference
        time_difference = end_datetime - start_datetime
        return time_difference

    def extract_time(self, chat_message):
        """
        Extract the time from a chat message.

        Args:
        chat_message (str): The chat message containing the timestamp.

        Returns:
        str: The extracted time.
        """
        # Define a regular expression pattern to match the timestamp
        pattern = r'(\d{2}/\d{2}/\d{2}), \d{2}:\d{2} -'

        # Use the regular expression to find the time
        match = re.search(pattern, chat_message)

        if match:
            time = match.group(1)
            return time
        else:
            return None
