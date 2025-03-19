import re
from datetime import datetime


def get_bangla_time_period(time_str):
    """
    Returns the Bangla time period (e.g. "সকাল", "রাত") based on the hour.
    It cleans the input time string by translating Bengali digits, removing trailing "টায়" and replacing AM/PM markers.
    """
    global time_obj
    bangla_to_english = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
    cleaned = time_str.translate(bangla_to_english).strip()
    cleaned = re.sub(r'\s*টায়\s*', '', cleaned)
    cleaned = cleaned.replace("এ.এম.", "AM").replace("পিএম", "PM")

    is_12h = "AM" in cleaned or "PM" in cleaned

    try:
        if is_12h:
            # Try multiple formats for 12-hour time
            for format_str in ["%I:%M:%S %p", "%I:%M %p"]:
                try:
                    time_obj = datetime.strptime(cleaned, format_str)
                    break
                except ValueError:
                    continue
            else:  # If all formats fail
                return "ভুল সময় বিন্যাস"
        else:
            # Try multiple formats for 24-hour time
            for format_str in ["%H:%M:%S", "%H:%M"]:
                try:
                    time_obj = datetime.strptime(cleaned, format_str)
                    break
                except ValueError:
                    continue
            else:  # If all formats fail
                return "ভুল সময় বিন্যাস"

        hour = time_obj.hour

        if 3 <= hour < 6:
            return "ভোর"
        elif 6 <= hour < 12:
            return "সকাল"
        elif 12 <= hour < 15:
            return "দুপুর"
        elif 15 <= hour < 18:
            return "বিকেল"
        elif 18 <= hour < 20:
            return "সন্ধ্যা"
        else:
            return "রাত"
    except Exception:
        return "ভুল সময় বিন্যাস"



print(get_bangla_time_period('07:30:45'))