from utils import process_whatsapp_log

if __name__ == "__main__":
    text_file = "chats/text/WhatsApp Chat with Lakshay.txt"
    json_file = text_file.replace(".txt", ".json").replace("text", "json")

    process_whatsapp_log(text_file)  # Convert multiline message into single line
