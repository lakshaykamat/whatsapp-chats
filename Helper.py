import json
from datetime import datetime


class Helper:
    @staticmethod
    def make_dates_consistent_in_json(input_file):
        """
        Process the chat JSON file and rewrite it with formatted dates.

        Args:
        input_file (str): Path to the input JSON file.
        """
        with open(input_file, "r+") as file:
            chat_data = json.load(file)
            file.seek(0)  # Reset file pointer to the beginning
            file.truncate()  # Clear file contents
            for message in chat_data:
                date_str = message["timestamp"]
                formatted_date = Helper.format_date(date_str)
                if formatted_date != "Invalid date format":
                    message["timestamp"] = formatted_date
                else:
                    print("Invalid date format")
            json.dump(chat_data, file, indent=4)

    @staticmethod
    def format_date(date_str):
        """
        Format the date string to "d/m/y" format with leading zeros added where necessary.

        Args:
        date_str (str): Date string.

        Returns:
        str: Formatted date string.
        """
        date_format = Helper.detect_date_format_with_time(date_str)
        if date_format:
            date_obj = datetime.strptime(date_str, date_format)
            formatted_date = date_obj.strftime("%d/%m/%y, %H:%M")
            return formatted_date
        else:
            return "Invalid date format"

    @staticmethod
    def detect_date_format_no_time(date_str: str):
        """
        Detect the date format of the input date string without considering time information.

        Args:
        date_str (str): Date string.

        Returns:
        str: Detected date format.
        """
        formats_to_try = ["%d/%m/%y", "%m/%d/%y"]

        for date_format in formats_to_try:
            try:
                datetime.strptime(date_str, date_format)
                return date_format
            except ValueError:
                pass

        return None  # Return None if no format matches

    @staticmethod
    def detect_date_format_with_time(date_str: str):
        """
        Detect the date format of the input date string including time information.

        Args:
        date_str (str): Date string.

        Returns:
        str: Detected date format.
        """
        formats_to_try = ["%d/%m/%y, %H:%M", "%m/%d/%y, %H:%M"]

        for date_format in formats_to_try:
            try:
                datetime.strptime(date_str, date_format)
                return date_format
            except ValueError:
                pass

        return None  # Return None if no format matches
