import json
from datetime import datetime

from convert_json import *


class Chat:
    def __init__(self, text_chat_file: str):
        self.text_chat_file: str = text_chat_file
        self.json_file: str = self.__get_json_file_path()
        convert_textchat_to_json(text_chat_file, self.json_file)

        self.chat_data: list = self.__load_chat_data()
        self.date_gap: datetime.timedelta = None
        self.sender_message_count: dict = {}
        self.sender_names: set = set()
        self.media_shared: dict = {}

        self.__process_chats()

    def __get_json_file_path(self) -> str:
        return self.text_chat_file.replace(".txt", ".json").replace("text", "json")

    def __load_chat_data(self) -> list:
        with open(self.json_file, "r") as json_file:
            return json.load(json_file)

    def __process_chats(self) -> None:
        self.__set_sender_names()
        self.__count_messages()
        self.__set_media_shared_count()
        self.__calculate_date_gap()

    def __set_sender_names(self) -> None:
        for item in self.chat_data:
            self.sender_names.add(item["sender"])

    def __set_media_shared_count(self) -> None:
        for item in self.chat_data:
            if "<Media omitted>" in item["message"]:
                self.media_shared[item["sender"]] = self.media_shared.get(item["sender"], 0) + 1

    def __count_messages(self) -> None:
        for item in self.chat_data:
            self.sender_message_count[item["sender"]] = self.sender_message_count.get(item["sender"], 0) + 1

    def __calculate_date_gap(self) -> None:
        date_format = "%d/%m/%y"
        first_message_date = datetime.strptime(self.chat_data[0]["timestamp"].split(",")[0], date_format).date()
        last_message_date = datetime.strptime(self.chat_data[-1]["timestamp"].split(",")[0], date_format).date()
        self.date_gap = abs(last_message_date - first_message_date)

    def get_date_difference(self):
        return self.date_gap

    def get_sender_names(self) -> set:
        return self.sender_names
