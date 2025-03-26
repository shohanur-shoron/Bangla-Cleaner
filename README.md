# Bangla-Cleaner
Okay, here is the revised `README.md` content following your specified structure: prioritizing `normalize_text`, then individual normalizers, then extractors, and highlighting the IPA and utility functions.

```markdown
# Bengali Text Normalizer (bengali-normalizer)

[![PyPI version](https://badge.fury.io/py/bengali-normalizer.svg)](https://badge.fury.io/py/bengali-normalizer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/bengali-normalizer.svg)](https://pypi.org/project/bengali-normalizer/)
<!-- Add other badges like build status if you set up CI/CD -->

A Python library designed to convert various written forms of Bengali text elements (like numbers, dates, times, currency, percentages, etc.) into their corresponding spoken word representations. This is particularly useful for:

*   **Text-to-Speech (TTS) Systems:** Preparing Bengali text for clearer and more natural-sounding speech synthesis.
*   **Natural Language Processing (NLP):** Standardizing text data for analysis or further processing.
*   **Data Cleaning:** Creating consistent textual representations from varied input formats.

The library handles both Bengali (০-৯) and Western (0-9) digits within the relevant contexts.

## Installation

You can install the library directly from PyPI using pip:

```bash
pip install bengali-normalizer
```

Make sure you have Python 3.7 or higher installed. The library depends on `python-dateutil`.

## Core Use Case: Comprehensive Normalization

The most common and recommended way to use this library is through the `normalize_text` function. It intelligently applies a sequence of normalization rules to handle various patterns within a given text, providing a fully normalized output string suitable for TTS or other NLP tasks.

```python
from bengali_normalizer import normalize_text

input_text = "আজকের তারিখ ১৫ জানুয়ারি, ২০২৫; অফিসের ফোন নম্বর হলো +৮৮০১৭১২৩৪৫৬৭৮ এবং মিটিং শুরু হবে ১০:৩০ AM টায়। দোকানে ছাড় চলছে ২০%, তাপমাত্রা ছিল ৩৫.৫°C, এবং দাম ৳৫০০ টাকা। অনুপাতটি ছিল ২:৩।"

normalized_text = normalize_text(input_text)

print(f"Original: {input_text}")
print(f"Normalized: {normalized_text}")

# Expected Output (may vary slightly based on conversion_data details):
# Original: আজকের তারিখ ১৫ জানুয়ারি, ২০২৫; অফিসের ফোন নম্বর হলো +৮৮০১৭১২৩৪৫৬৭৮ এবং মিটিং শুরু হবে ۱۰:৩০ AM টায়। দোকানে ছাড় চলছে ২০%, তাপমাত্রা ছিল ৩৫.৫°C, এবং দাম ৳৫০০ টাকা। অনুপাতটি ছিল ২:৩।
# Normalized: আজকের তারিখ পনেরোই জানুয়ারি দুই হাজার পঁচিশ; অফিসের ফোন নম্বর হলো প্লাস আট আট শূন্য এক সাত এক দুই তিন চার পাঁচ ছয় সাত আট এবং মিটিং শুরু হবে সকাল দশ টা ত্রিশ মিনিটে এ। দোকানে ছাড় চলছে বিশ শতাংশ, তাপমাত্রা ছিল পঁয়ত্রিশ দশমিক পাঁচ ডিগ্রি সেলসিয়াস, এবং দাম পাঁচশো টাকা। অনুপাতটি ছিল দুই অনুপাত তিন।
```

The `normalize_text` function internally uses a pipeline of specific normalizers in an optimal order to prevent conflicts (e.g., normalizing dates before general numbers).

## Features & Individual Normalizer Functions

While `normalize_text` is the primary entry point, the library also exposes individual normalizer functions. You can use these if you need to normalize only specific types of elements within your text. Each normalizer function takes the input text and returns the text with only that specific element type normalized.

---

### 1. `normalize_dates(text)`

*   Converts date strings (various formats, Bengali/English digits/months) into spoken Bengali words.
*   **Example Formats:** `১৫ জানুয়ারি, ২০২৫`, `২৮শে ডিসেম্বর ২০২৪`, `০৫-০৫-১৯৯৫`, `২২/মার্চ/২০২৫`, `25 December 2024`, `২০২৫-০৮-৩০`

```python
from bengali_normalizer import normalize_dates

text = "গুরুত্বপূর্ণ তারিখগুলো হলো ০৫-০৫-১৯৯৫ এবং আগামী ২২/মার্চ/২০২৫।"
normalized_text = normalize_dates(text)
print(f"Normalized Dates Only: {normalized_text}")
# Expected: Normalized Dates Only: গুরুত্বপূর্ণ তারিখগুলো হলো পাঁচই মে উনিশশো পঁচানব্বই এবং আগামী বাইশে মার্চ দুই হাজার পঁচিশ।
```

---

### 2. `normalize_phonenumbers(text)`

*   Converts standard Bangladeshi mobile numbers into digit-by-digit spoken words (e.g., "শূন্য এক সাত..."). Handles optional `+88` prefix and hyphens.
*   **Example Formats:** `০১৭১২৩৪৫৬৭৮`, `+৮৮০১৭১২৩৪৫৬৭৮`, `01712-345678`, `+8801612345677`

```python
from bengali_normalizer import normalize_phonenumbers

text = "যোগাযোগ করুন ০১৭১২-৩৪৫৬৭৮ অথবা +৮৮০১৬১২৩৪৫৬৭৭ নম্বরে।"
normalized_text = normalize_phonenumbers(text)
print(f"Normalized Phone Numbers Only: {normalized_text}")
# Expected: Normalized Phone Numbers Only: যোগাযোগ করুন শূন্য এক সাত এক দুই তিন চার পাঁচ ছয় সাত আট অথবা প্লাস আট আট শূন্য এক ছয় এক দুই তিন চার পাঁচ ছয় সাত সাত নম্বরে।
```

---

### 3. `normalize_time(text)`

*   Converts time expressions (HH:MM:SS, AM/PM variations, optional "টায়") into spoken Bengali format (e.g., "সকাল দশটা ত্রিশ মিনিট").
*   **Example Formats:** `১০:০০ AM`, `১৯:৪৫:০০`, `৯:৩০ মিনিটে`, `3:45 PM`, `১২:০০ PM টায়`, `8:00 P.M.`

```python
from bengali_normalizer import normalize_time

text = "মিটিং শুরু হবে ১০:৩০ AM টায় এবং শেষ হবে ৪:০০ PM এ।"
normalized_text = normalize_time(text)
print(f"Normalized Times Only: {normalized_text}")
# Expected: Normalized Times Only: মিটিং শুরু হবে সকাল দশ টা ত্রিশ মিনিটে এ এবং শেষ হবে বিকেল চার টা শূন্য মিনিটে এ।
```

---

### 4. `normalize_taka(text)`

*   Converts Bangladeshi Taka currency expressions into spoken words. Handles "৳", "টাকা", "টাকার", commas, decimals, and units like "লক্ষ"/"কোটি".
*   **Example Formats:** `৳৫০০`, `২৫০ টাকা`, `১০ টাকার`, `৳১,২৩,৪৫৬.৭৮`, `৳১০ লক্ষ টাকা`

```python
from bengali_normalizer import normalize_taka

text = "খরচ হয়েছে ৳৫০০ টাকা এবং বাজেট ছিল ১ লক্ষ টাকার।"
normalized_text = normalize_taka(text)
print(f"Normalized Taka Amounts Only: {normalized_text}")
# Expected: Normalized Taka Amounts Only: খরচ হয়েছে পাঁচশো টাকা এবং বাজেট ছিল এক লক্ষ টাকার।
```

---

### 5. `normalize_percentage(text)`

*   Converts percentage values (followed by "%" or "শতাংশ") into spoken words (using "শতাংশ").
*   **Example Formats:** `২০%`, `১৫.৫ শতাংশ`, `75.5%`, `-১০%`

```python
from bengali_normalizer import normalize_percentage

text = "ছাড় চলছে ২০% এবং লাভ হয়েছে ৭.৫ শতাংশ।"
normalized_text = normalize_percentage(text)
print(f"Normalized Percentages Only: {normalized_text}")
# Expected: Normalized Percentages Only: ছাড় চলছে বিশ শতাংশ এবং লাভ হয়েছে সাত দশমিক পাঁচ শতাংশ।
```

---

### 6. `normalize_temperatures(text)`

*   Converts temperature values associated with units like "°C", "°F", "ডিগ্রি সেলসিয়াস", etc., into spoken words. Handles negative values.
*   **Example Formats:** `৩৫°C`, `৩২.৫ ডিগ্রি সেলসিয়াস`, `98.6°F`, `-৫°C`, `৪০ ডিগ্রি`

```python
from bengali_normalizer import normalize_temperatures

text = "আজকের তাপমাত্রা ৩৫°C এবং সর্বনিম্ন ছিল -২ ডিগ্রি সেলসিয়াস।"
normalized_text = normalize_temperatures(text)
print(f"Normalized Temperatures Only: {normalized_text}")
# Expected: Normalized Temperatures Only: আজকের তাপমাত্রা পঁয়ত্রিশ ডিগ্রি সেলসিয়াস এবং সর্বনিম্ন ছিল মাইনাস দুই ডিগ্রি সেলসিয়াস।
```

---

### 7. `normalize_ratio(text)`

*   Converts ratio expressions into spoken words, typically using "অনুপাত" or "থেকে" as separators.
*   **Example Formats:** `১:৩`, `৫:৩:১`, `২.৫:১`, `১ঃ১০০`, `৭-৩`, `১ থেকে ৫`, `১ অনুপাত ৫`

```python
from bengali_normalizer import normalize_ratio

text = "মিশ্রণটি ১:৩ অনুপাতে তৈরি করুন। রেঞ্জ হলো ১ থেকে ৫।"
normalized_text = normalize_ratio(text)
print(f"Normalized Ratios Only: {normalized_text}")
# Expected: Normalized Ratios Only: মিশ্রণটি এক অনুপাত তিন অনুপাতে তৈরি করুন। রেঞ্জ হলো এক থেকে পাঁচ।
```

---

### 8. `normalize_ordinal(text)`

*   Converts ordinal numbers (e.g., "১ম", "২য়", "3rd", "১লা") into their spoken word equivalents ("প্রথম", "দ্বিতীয়", "পহেলা").
*   **Example Formats:** `১ম`, `২য়`, `3rd`, `৪র্থ`, `১০ম`, `১লা`, `৩রা`, `২২শে`, `10,000তম`

```python
from bengali_normalizer import normalize_ordinal

text = "তিনি পরীক্ষায় ১ম স্থান এবং ৩য় পুরস্কার পেয়েছেন। আজ মাসের ১লা দিন।"
normalized_text = normalize_ordinal(text)
print(f"Normalized Ordinals Only: {normalized_text}")
# Expected: Normalized Ordinals Only: তিনি পরীক্ষায় প্রথম স্থান এবং তৃতীয় পুরস্কার পেয়েছেন। আজ মাসের পহেলা দিন।
```

---

### 9. `normalize_year(text)`

*   Converts 4-digit year expressions, including context words like "সাল" or "সন", into spoken words.
*   **Example Formats:** `২০২৫ সাল`, `সাল ১৯৭১`, `১৯৪৫ সন`, `2024`

```python
from bengali_normalizer import normalize_year

text = "এটি ঘটেছিল ১৯৭১ সালে এবং পরিকল্পনাটি ২০২৫ সালের।"
normalized_text = normalize_year(text)
print(f"Normalized Years Only: {normalized_text}")
# Expected: Normalized Years Only: এটি ঘটেছিল উনিশশো একাত্তর সালে এবং পরিকল্পনাটি দুই হাজার পঁচিশ সালের।
```

---

### 10. `normalize_numbers(text)`

*   Converts standalone integers and floating-point numbers (Bengali/English digits, commas, negatives) into spoken words.
*   **Note:** This is applied last in the `normalize_text` pipeline to avoid conflicts with specific patterns already handled by other normalizers.
*   **Example Formats:** `১০০`, `45`, `২.৫`, `-১০.৭৫`, `১,২৩,৪৫৬`

```python
from bengali_normalizer import normalize_numbers

# Note: Numbers within dates, times, etc., would be handled by their respective normalizers first in normalize_text.
text = "মোট নম্বর ছিল ১০০ এবং গড় ছিল ৭৫.৫ কেজি।"
normalized_text = normalize_numbers(text)
print(f"Normalized Numbers Only: {normalized_text}")
# Expected: Normalized Numbers Only: মোট নম্বর ছিল একশো এবং গড় ছিল পঁচাত্তর দশমিক পাঁচ কেজি।
```

---

## Extractor Functions

For advanced users or specific tasks, the library also exposes functions used to *detect* (extract) patterns without necessarily normalizing them. These functions return a list of strings matching the specific pattern found in the text. They are primarily used internally by the normalizer functions.

*   `extract_bengali_dates(text)`
*   `extract_mobile_numbers(text)`
*   `extract_time(text)`
*   `extract_taka_amounts(text)`
*   `extract_percentages(text)`
*   `extract_temperatures(text)`
*   `extract_ratios(text)`
*   `extract_ordinals(text)`
*   `extract_years_with_context(text)`
*   `extract_numbers(text)`

**Example: Extracting only Taka amounts**

```python
from bengali_normalizer import extract_taka_amounts

text = "দাম ৳৫০০ এবং ছাড় ৳৫০.২৫ টাকা।"
amounts = extract_taka_amounts(text)
print(amounts)
# Expected: ['৳৫০০', '৳৫০.২৫ টাকা']
```

---

## Phonetic Conversion (IPA)

The library includes a basic utility function `bangla_to_ipa_converter` to attempt converting Bengali text (including normalized output) into the International Phonetic Alphabet (IPA). This functionality depends heavily on predefined mappings for individual characters and common conjuncts (`যুক্তাক্ষর`) within the `conversion_data.py` file.

**Note:** This is a rule-based converter and may not cover all phonetic nuances or exceptions in Bengali pronunciation. Its accuracy depends on the completeness of the internal mapping tables.

```python
# Ensure you have the function accessible (it's in utils.py, not directly exposed in __init__.py by default)
# You might need to import it specifically if needed:
# from bengali_normalizer.utils import bangla_to_ipa_converter
# Or modify __init__.py to expose it.

# Assuming it's exposed or imported:
# from bengali_normalizer import bangla_to_ipa_converter

# Example (conceptual, actual output depends on internal IPA maps)
# text = "বাংলা"
# ipa_text = bangla_to_ipa_converter(text)
# print(f"{text} -> {ipa_text}")
# Example Output (depends heavily on mapping): bɑŋlɑ
```

---

## Utility Functions (`utils.py`)

Several helper functions reside in `bengali_normalizer.utils`. These handle tasks like:

*   Converting between Bengali and English digits (`bangla_to_english_number`).
*   Parsing date components (`extract_date_components_bangla`).
*   Determining time periods (`get_bangla_time_period`).
*   Separating year components (`separate_year`).
*   Cleaning extra spaces (`remove_extra_spaces`).
*   Phonetic conversion (`bangla_to_ipa_converter`).

These are primarily intended for internal use by the normalizer and extractor functions, but advanced users might find them useful for specific tasks. Direct use requires importing them specifically from `bengali_normalizer.utils`.

---

## Internal Data (`conversion_data.py`)

The accuracy and scope of the normalization rely heavily on an internal module `bengali_normalizer.conversion_data`. This file contains essential dictionaries mapping:

*   Digits and numbers (0-100+) to Bengali words.
*   Month names (Bengali to English for parsing).
*   Day names (1-31, using spoken ordinal forms like 'পহেলা', 'দোসরা', 'একুশে').
*   Ordinal suffixes ('১ম' -> 'প্রথম', etc.).
*   Basic phonetic mappings (for IPA conversion).

While not meant for direct user editing, understanding its role is key to the library's function. Missing or incorrect entries in this file will lead to incorrect normalization.

## Contributing

Contributions are welcome! If you find a bug, have a suggestion for improvement, or want to add support for more normalization patterns, please:

1.  Check the [Issue Tracker]([URL to your issue tracker]) to see if the issue already exists.
2.  If not, open a new issue describing the problem or suggestion.
3.  For code contributions, please fork the repository, create a new branch for your feature or bugfix, and submit a pull request. Please include tests for your changes if possible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!--
## Acknowledgements (Optional)
* Mention any inspirations or libraries you adapted from.
-->
```
