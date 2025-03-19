import re


def extract_mobile_numbers(text):
    # This pattern matches numbers in two formats:
    # 1. 11-digit format: starts with 0 followed by one of the valid prefixes (e.g., 013, 014, etc.) and 8 additional digits.
    # 2. 14-digit format: starts with +88, then a 0, a valid prefix, and 8 additional digits.
    # Using negative lookbehind (?<!\d) and negative lookahead (?!\d) ensures that the match is not part of a longer number.
    mobile_pattern = r'(?<!\d)(?:\+88)?(?:013|014|015|016|017|018|019)\d{8}(?!\d)'

    # Find all matching mobile numbers
    return re.findall(mobile_pattern, text)


def extract_bengali_dates(text):
    bengali_months = r'(?:জানুয়ারি|ফেব্রুয়ারি|মার্চ|এপ্রিল|মে|জুন|জুলাই|আগস্ট|সেপ্টেম্বর|অক্টোবর|নভেম্বর|ডিসেম্বর)'

    date_pattern = rf'''
        (?<!\d)  # Ensure it's not part of a larger number
        (
            # Textual date with optional suffix and comma (e.g., ২৮ ডিসেম্বর, ২০২৪)
            [০-৯]{{1,2}}(?:লা|ই|শে|ঠা|এ)?\s+{bengali_months}\s*,?\s*[০-৯]{{3,4}}
            |
            # Textual date with separators (e.g., ১৫/ফেব্রুয়ারি/২০২৪)
            [০-৯]{{1,2}}[/-]{bengali_months}[/-][০-৯]{{3,4}}
            |
            # Numeric DD-MM-YYYY or DD/MM/YYYY with same separator
            [০-৯]{{1,2}}[-/][০-৯]{{1,2}}[-/][০-৯]{{3,4}}
            |
            # Numeric YYYY-MM-DD or YYYY/MM/DD with same separator
            [০-৯]{{4}}[-/][০-৯]{{1,2}}[-/][০-৯]{{1,2}}
        )
        (?=\s|,|$|।)  # Lookahead for boundary
    '''

    return re.finditer(date_pattern, text, re.VERBOSE)


