from datetime import datetime, timedelta
import re
from typing import Optional


class Time:
    @staticmethod
    def format_time(time) -> str:
        """
        Convert a timedelta object to a human-readable form.

        Args:
        time (timedelta): The timedelta object.

        Returns:
        str: A string representing the duration in human-readable form.
        """
        # Calculate the total number of seconds in the timedelta
        total_seconds: int = int(time.total_seconds())

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

    @staticmethod
    def extract_time(chat_message: str) -> Optional[str]:
        """
        Extract the time from a chat message.

        Args:
        chat_message (str): The chat message containing the timestamp.

        Returns:
        Optional[str]: The extracted time if found, otherwise None.
        """
        # Define a regular expression pattern to match the timestamp
        pattern = r'(\d{2}/\d{2}/\d{2}), \d{2}:\d{2} -'

        # Use the regular expression to find the time
        match = re.search(pattern, chat_message)

        if match:
            time = match.group(1)
            return time
        else:
            return None

    @staticmethod
    def calculate_time_difference(start_time: str, end_time: str) -> timedelta:
        """
        Calculate the time difference between two timestamps.

        Args:
        start_time (str): The start timestamp in the format "YY/MM/DD".
        end_time (str): The end timestamp in the format "YY/MM/DD".

        Returns:
        timedelta: The time difference between the two timestamps.
        """
        # Convert the timestamps to datetime objects
        start_datetime: datetime = datetime.strptime(start_time, "%d/%m/%y")
        end_datetime: datetime = datetime.strptime(end_time, "%d/%m/%y")

        # Ensure start time is before end time
        if start_datetime > end_datetime:
            start_datetime, end_datetime = end_datetime, start_datetime

        # Calculate the time difference
        time_difference: timedelta = end_datetime - start_datetime
        return time_difference
