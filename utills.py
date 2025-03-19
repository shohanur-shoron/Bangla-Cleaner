from number_in_word import *
from dateutil.parser import parse
import re
import subprocess
from datetime import datetime

def separate_year(bengali_number):
    bengali_to_english = {
        '০': '0', '১': '1', '২': '2', '৩': '3', '৪': '4',
        '৫': '5', '৬': '6', '৭': '7', '৮': '8', '৯': '9'
    }
    english_number = ''.join(bengali_to_english[digit] for digit in str(bengali_number))
    num1 = int(english_number) // 100 * 100
    num2 = int(english_number) % 100
    return num1, num2


def extract_date_components_bangla(bangla_date):
    bangla_to_english_digits = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
    english_to_bangla_digits = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

    try:
        for bangla_month, english_month in bangla_months.items():
            bangla_date = bangla_date.replace(bangla_month, english_month)

        # Convert Bangla digits to English digits
        bangla_date = bangla_date.translate(bangla_to_english_digits)

        # Parse the processed date
        parsed_date = parse(bangla_date, dayfirst=True, fuzzy=True)
        day = str(parsed_date.day).translate(english_to_bangla_digits)
        month = list(bangla_months.keys())[list(bangla_months.values()).index(parsed_date.strftime("%B"))]
        year = str(parsed_date.year).translate(english_to_bangla_digits)
        return day, month, year
    except Exception as e:
        return f"Error: {str(e)}"

