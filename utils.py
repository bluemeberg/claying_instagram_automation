from datetime import datetime, timedelta
import re

def change_date(date) :
    date_obj = datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
    # Get the current date and time
    now = datetime.now()

    # Calculate the difference
    difference = now - date_obj

    # Convert the difference into days, months, and years
    days = difference.days
    hours = difference.seconds // 3600  # converting seconds to hours
    months = days // 30
    years = days // 365

    # Creating a string representation
    if years > 0:
        result = f"{years}년 전"
    elif months > 0:
        result = f"{months}달 전"
    elif days > 0:
        result = f"{days}일 전"
    else:
        result = f"{hours}시간 전"
    return result

def convert_number_format(number):
    int_number = int(number)
    if int_number >= 10000:
        return f"{int_number/1000:.1f}만개"
    elif int_number >= 1000:
        return f"{int_number/1000:.1f}천개"
    else:
        return f"{int_number}개"

def extract_text_inside_braces(text):
    """
    Extract the text inside the curly braces.

    :param text: The original text containing curly braces.
    :return: The text inside the curly braces.
    """
    # Using regular expression to find text inside curly braces
    match = re.search(r'\{(.+?)\}', text)
    if match:
        return match.group(1)
    else:
        return "No text found inside braces"

def parse_duration(duration_str):
    """
    Parses a duration string from YouTube API and returns the total duration in seconds.
    Handles various combinations including hours, minutes, and seconds.
    """
    # Regular expression to extract the hours, minutes, and seconds
    pattern = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?')
    parts = pattern.match(duration_str)

    hours = int(parts.group(1)) if parts.group(1) else 0
    minutes = int(parts.group(2)) if parts.group(2) else 0
    seconds = int(parts.group(3)) if parts.group(3) else 0

    return hours * 3600 + minutes * 60 + seconds
