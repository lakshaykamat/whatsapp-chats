import json


class WhatsAppChat:
    def __init__(self, json_chat_file: str):
        self.json_chat_file = json_chat_file
        self.chat_data: list = self.__load_chat_data()

    def __str__(self):
        return f"WhatsAppChat(json_chat_file='{self.json_chat_file}')"

    def __load_chat_data(self) -> list:
        with open(self.json_chat_file, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
