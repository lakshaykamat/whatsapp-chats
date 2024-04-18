# WhatsApp Chats Analysis

![WhatsApp Logo](https://static.whatsapp.net/rsrc.php/v3/yR/r/y8-PTBaP90a.png)

This program analyzes WhatsApp messages exchanged between you and your friends. It provides insights into message counts, media sharing, and other interesting statistics.

## How to Use

1. **Export Your Chats**: Start by exporting your chats from WhatsApp without including media files.

2. **Run the Program**: Execute the program by providing the path to your exported chat file.

3. **View Results**: Once the analysis is complete, view the generated report to see various statistics about your chats.

## Features

- **Message Count**: See how many messages each participant has sent.
- **Media Sharing**: Check how many media files (images, videos, etc.) each participant has shared.
- **Date Analysis**: Find out the duration of your chat history.
- **CLI Support**: Command-line interface allows easy usage without any complex setup.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/whatsapp-chat-analysis.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the program using the following command:

```bash
python analyze_chats.py path_to_your_chat_file.txt
```

Replace `path_to_your_chat_file.txt` with the path to your exported chat file.

## Example Output

```text
-----------------------------------------
WhatsApp Chat Analysis Report
-----------------------------------------

- Message Count -
Alice: 350 messages
Bob: 248 messages
Charlie: 173 messages

- Media Sharing -
Alice: 20 media files
Bob: 15 media files
Charlie: 8 media files

- Chat Duration -
Total days: 112 days
```

## Contributing

Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.