from datetime import datetime
import matplotlib.pyplot as plt

from Chat import ChatAnalyzer
from Time import Time


def format_month(month_str: str) -> str:
    """
    Convert a date string in the format "YYYY-MM" to "MM/YY" format.

    Args:
        month_str (str): Date string in the format "YYYY-MM".

    Returns:
        str: Date string in the format "MM/YY".
    """
    highest_month_date = datetime.strptime(month_str, "%Y-%m")
    formatted_highest_month = highest_month_date.strftime("%m/%y")
    return formatted_highest_month


def show_monthly_graph(monthly_data: dict, title: str):
    """
    Display the monthly message counts as a graph.

    Args:
        monthly_data (dict): Dictionary containing monthly message counts.
        title (str): Title for the graph.
    """
    plt.plot(monthly_data.keys(), monthly_data.values(), color='green', linestyle='-', marker='o', markersize=5,
             label='Message')
    plt.xlabel("Months", fontsize=12, fontweight='bold', color='black')
    plt.ylabel("Messages", fontsize=12, fontweight='bold', color='black')
    plt.title(title, fontsize=14, fontweight='bold', color='black')

    # plt.plot(x_values, y_values, color='blue', linestyle='-', marker='o', markersize=5, label='Data')
    # plt.xlabel('X-axis Label', fontsize=12, fontweight='bold', color='black')
    # plt.ylabel('Y-axis Label', fontsize=12, fontweight='bold', color='black')
    # plt.title('Customized Plot', fontsize=14, fontweight='bold', color='black')
    plt.xticks(fontsize=10, color='gray', rotation=45)
    plt.yticks(fontsize=10, color='gray')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.legend(loc='upper right', fontsize=10)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    chat_analyzer = ChatAnalyzer("chats/text/WhatsApp Chat with Asad.txt")

    # Print basic chat statistics
    print("Sender Names:", chat_analyzer.get_sender_names())
    print("Sender Message Count:", chat_analyzer.sender_message_count)
    print("Media Shared:", chat_analyzer.get_media_shared())
    # print(f"Date Gap: {Time.format_time(chat_analyzer.date_gap)} ({chat_analyzer.date_gap})")

    # print(chat_analyzer.get_monthly_counts())
    highest_month = max(chat_analyzer.get_monthly_counts(), key=chat_analyzer.get_monthly_counts().get)
    highest_month_messages = chat_analyzer.get_monthly_counts()[highest_month]
    highest_month_formatted = format_month(highest_month)
    message_count_by_highest_month = chat_analyzer.message_count_by_month(month=highest_month_formatted)

    # Display the graph for the highest month's message counts
    show_monthly_graph(message_count_by_highest_month, f"Messages in the highest month ({highest_month_formatted})")

    # Display the graph for overall monthly message counts
    names = ", ".join(chat_analyzer.get_sender_names())
    show_monthly_graph(chat_analyzer.get_monthly_counts(), f"Overall Monthly Messages of {names}")
