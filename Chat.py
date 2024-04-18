import json
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any, Tuple, Dict

from Helper import Helper
from convert_json import convert_textchat_to_json


class ChatAnalyzer:
    def __init__(self, text_chat_file: str):
        self.text_chat_file: str = text_chat_file
        self.json_file: str = self._get_json_file_path()
        convert_textchat_to_json(input_file=text_chat_file, output_file=self.json_file)
        Helper.make_dates_consistent_in_json(self.json_file)
        self.chat_data: list = self._load_chat_data()
        # self.date_gap = None
        self.sender_message_count: dict = {}
        self.sender_names: Tuple[str, ...] = ()
        self.media_shared: dict = {}
        self.monthly_counts_of_user: Dict[str, dict] = defaultdict(lambda: defaultdict(int))
        self.monthly_counts: dict = {}

        self._process_chats()

    def _get_json_file_path(self) -> str:
        return self.text_chat_file.replace(".txt", ".json").replace("text", "json")

    def _load_chat_data(self) -> list:
        with open(self.json_file, "r") as json_file:
            return json.load(json_file)

    def _process_chats(self) -> None:
        self._set_sender_names()
        self._count_messages()
        self._set_media_shared_count()
        # self._calculate_date_gap()
        self._count_monthly_chats()

    def _set_sender_names(self) -> None:
        self.sender_names = tuple(set(message["sender"] for message in self.chat_data))

    def _count_messages(self) -> None:
        sender_message_counts = Counter(message["sender"] for message in self.chat_data)
        self.sender_message_count.update(sender_message_counts)
        total_messages = sum(sender_message_counts.values())
        self.sender_message_count["total"] = total_messages

    def _calculate_date_gap(self) -> None:
        first_date = self.chat_data[0]["timestamp"].split(",")[0]
        last_date = self.chat_data[-1]["timestamp"].split(",")[0]

        date_format = Helper.detect_date_format_no_time(last_date)
        first_message_date = datetime.strptime(first_date, date_format).date()
        last_message_date = datetime.strptime(last_date, date_format).date()

        self.date_gap = abs(last_message_date - first_message_date)

    def _set_media_shared_count(self) -> None:
        for message in self.chat_data:
            if "<Media omitted>" in message["message"]:
                name = message["sender"]
                self.media_shared[name] = self.media_shared.get(name, 0) + 1

    def message_count_by_month(self, month: str) -> dict:
        """
        Count the messages for each month.

        Args:
            month (str): Month in "MM/YY" format.

        Returns:
            dict: Message counts for the specified month.
        """
        message_count_by_month = {}
        for chat in self.chat_data:
            if month in chat["timestamp"]:
                month_key = chat["timestamp"].split(",")[0]
                message_count_by_month[month_key] = message_count_by_month.get(month_key, 0) + 1
        return message_count_by_month

    def _count_monthly_chats(self) -> None:
        for message in self.chat_data:
            timestamp = message["timestamp"]
            sender = message["sender"]
            message_date = datetime.strptime(timestamp, Helper.detect_date_format_with_time(timestamp))
            month_year = message_date.strftime("%Y-%m")
            self.monthly_counts_of_user[sender][month_year] = self.monthly_counts_of_user[sender].get(month_year, 0) + 1

        for item in self.monthly_counts_of_user:
            for month in self.monthly_counts_of_user[item]:
                self.monthly_counts.setdefault(month, 0)
                self.monthly_counts[month] += self.monthly_counts_of_user[item][month]

    def get_date_difference(self) -> Any:
        return self.date_gap

    def get_sender_names(self) -> Tuple[str, ...]:
        return self.sender_names

    def get_media_shared(self) -> dict:
        return self.media_shared

    def get_monthly_counts(self) -> dict:
        return self.monthly_counts
