from Chat import Chat


if __name__ == "__main__":
    chat = Chat("chats/text/WhatsApp Chat with Anu.txt")
    print(chat.get_sender_names())
    print(chat.sender_message_count)
    print(chat.media_shared)
    print(chat.date_gap)

