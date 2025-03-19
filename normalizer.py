from methods import *
from exteactor import *

#todo abbreviation

def normalize_dates(text):
    matches = extract_bengali_dates(text)
    matches = sorted(matches, key=len, reverse=True)
    for match in matches:
        date_text = match.group(1)  # Extract matched date
        normalized_date = date_to_word(date_text)  # Convert to word form
        text = text.replace(date_text, normalized_date)  # Replace in sentence

    return text

