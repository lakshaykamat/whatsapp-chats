from Chats import Chats
from Time import Time


chat_processor = Chats("chats/example.txt")
info = chat_processor.get_message_count_info()

print(chat_processor.sender_message_count)
print(chat_processor.time_gap)
print(chat_processor.chat_file)
print(chat_processor.sender_names)
print(info)
