from Time import Time
import re
from typing import List, Dict


class Chats:
    def __init__(self, chat_file: str) -> None:
        self.time_gap: Time = None
        self.chat_file: str = chat_file
        self.sender_message_count: Dict[str, int] = {}
        self.sender_names: set = set()
        self.__process_chat_file()

    def __process_chat_file(self) -> None:
        """
        Process the chat file to count messages from each sender and get sender names.
        """
        lines: List[str] = self.__read_chat_file()
        first_message_time: str = Time.extract_time(lines[0])
        last_message_time: str = Time.extract_time(lines[-1])
        self.time_gap: Time = Time.calculate_time_difference(last_message_time, first_message_time)
        self.__parse_messages(lines)

    def __read_chat_file(self) -> List[str]:
        """
        Read the chat file and return its contents as a list of lines.
        """
        with open(self.chat_file, 'r', encoding='utf-8') as file:
            lines: List[str] = file.readlines()
        return lines

    def get_message_count_info(self) -> str:
        """
        Get information about message counts.

        Returns:
        str: A string containing information about the sender who sent the most messages and the difference in message counts.
        """
        max_sender: str = None
        max_count: int = float('-inf')  # Initialize to negative infinity
        second_max_sender: str = None
        second_max_count: int = float('-inf')  # Initialize to negative infinity

        # Find the sender with the highest and second-highest message counts
        for sender, count in self.sender_message_count.items():
            if count > max_count:
                second_max_sender = max_sender
                second_max_count = max_count
                max_sender = sender
                max_count = count
            elif count > second_max_count:
                second_max_sender = sender
                second_max_count = count

        # Calculate the difference in message counts
        difference: int = max_count - second_max_count

        # Construct the information string
        info_string: str = (
            f"{max_sender} sent the most messages with a count of {max_count}. \n"
            f"The messages difference between the {max_sender} and {second_max_sender} is {difference}."
        )

        return info_string

    def __parse_messages(self, lines: List[str]) -> None:
        """
        Parse each line of the chat file to extract sender names and count messages.
        """
        pattern: str = r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - ([^:]+):'
        for line in lines:
            match = re.match(pattern, line)
            if match:
                sender: str = match.group(1)
                self.sender_names.add(sender)
                self.sender_message_count[sender] = self.sender_message_count.get(sender, 0) + 1
