from ChatProcessor import ChatProcessor


def format_time(time):
    """
    Convert a timedelta object to a human-readable form.

    Args:
    timedelta_obj (timedelta): The timedelta object.

    Returns:
    str: A string representing the duration in human-readable form.
    """
    # Calculate the total number of seconds in the timedelta
    total_seconds = int(time.total_seconds())

    # Calculate the number of years, months, days, hours, minutes, and seconds
    years, total_seconds = divmod(total_seconds, 31536000)  # 60 * 60 * 24 * 365
    months, total_seconds = divmod(total_seconds, 2592000)  # 60 * 60 * 24 * 30
    days, total_seconds = divmod(total_seconds, 86400)  # 60 * 60 * 24
    hours, total_seconds = divmod(total_seconds, 3600)  # 60 * 60
    minutes, seconds = divmod(total_seconds, 60)

    parts = []
    if years:
        parts.append(f"{years} {'year' if years == 1 else 'years'}")
    if months:
        parts.append(f"{months} {'month' if months == 1 else 'months'}")
    if days:
        parts.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours:
        parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds:
        parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return ' and '.join(parts)
    else:
        return ', '.join(parts[:-1]) + f', and {parts[-1]}'


def message_count_info(message_counts: dict):
    max_sender = None
    max_count = float('-inf')  # Initialize to negative infinity
    second_max_sender = None
    second_max_count = float('-inf')  # Initialize to negative infinity

    # Iterate over the key-value pairs in the dictionary
    for sender, count in message_counts.items():
        # Check if the current sender has a higher message count
        if count > max_count:
            second_max_sender = max_sender
            second_max_count = max_count
            max_sender = sender
            max_count = count
        elif count > second_max_count:
            second_max_sender = sender
            second_max_count = count

    # Calculate the difference in message counts
    difference = max_count - second_max_count

    # Format the information into a string
    info_string = (
        f"The user '{max_sender}' sent the most messages with a count of {max_count}. "
        f"The difference between the highest and second-highest message counts is {difference}."
    )

    return info_string


file_path = "chats/WhatsApp Chat with goshblue6721.txt"
chat_processor = ChatProcessor(file_path)
chat_processor.process_chat_file()
info = message_count_info(chat_processor.sender_message_count)
