# Bangla-Cleaner

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

# Bengali Normalizer Extractors

This document describes the extractor functions found within the `bengali_normalizer.extractor` module. These functions are designed to **detect and extract specific patterns** from Bengali text, such as dates, phone numbers, currency amounts, etc., using regular expressions.

They are primarily used internally by the normalizer functions (`normalizer.py`) to identify which parts of the text need conversion. However, you can import and use these functions directly if your task only requires *finding* these patterns without necessarily converting them to words.

**Key Features of Extractors:**

*   Each function targets a specific type of textual element.
*   They typically return a list of strings, where each string is a detected match found in the input text.
*   They are designed to handle variations in formatting, including both Bengali (০-৯) and Western (0-9) digits where applicable.
*   The regular expressions aim for accuracy but might occasionally have edge cases or limitations depending on the complexity and ambiguity of the text.

## Importing Extractors

To use these functions directly, import them from the `extractor` submodule:

```python
from bengali_normalizer.extractor import extract_mobile_numbers, extract_bengali_dates
# Import other functions as needed
```

---

## Function Descriptions and Examples

### 1. `extract_mobile_numbers(text)`

*   **Description:** Finds potential Bangladeshi mobile phone numbers in the text. It looks for standard prefixes (013-019 or ০১৩-০১৯), allows for an optional `+88` or `+৮৮` prefix, and handles an optional hyphen in the common `NNN-NNNNNN` format. It tries to avoid matching invalid sequences or numbers embedded within other words/codes.
*   **Supported Formats (Examples):** `০১৭১২৩৪৫৬৭৮`, `+৮৮০১৭১২৩৪৫৬৭৮`, `01712-345678`, `+8801612345677`
*   **Returns:** `list[str]` - A list of matched phone number strings.

```python
from bengali_normalizer.extractor import extract_mobile_numbers

text = "তার নম্বর 01712345678 এবং অন্যটি +৮৮০১৯৮৭-৬৫৪৩২১।"
numbers = extract_mobile_numbers(text)
print(f"Mobile numbers found: {numbers}")

# Expected Output:
# Mobile numbers found: ['01712345678', '+৮৮০১৯৮৭-৬৫৪৩২১']
```

---

### 2. `extract_bengali_dates(text)`

*   **Description:** Detects and extracts date expressions written in various common formats. It supports Bengali and English month names, Bengali and English digits, and different separators (`-`, `/`, space, comma). It also handles common Bengali date suffixes (like 'শে', 'ই', 'লা') and English ordinal suffixes ('st', 'nd', 'rd', 'th').
*   **Supported Formats (Examples):** `১৫ জানুয়ারি, ২০২৫`, `২৮শে ডিসেম্বর ২০২৪`, `০৫-০৫-১৯৯৫`, `২২/মার্চ/২০২৫`, `25 December 2024`, `2024-12-31`, `৩০/১২/২০২৫`
*   **Returns:** `list[str]` - A list of matched date strings.

```python
from bengali_normalizer.extractor import extract_bengali_dates

text = "মিটিং হবে ১৫ জানুয়ারি, ২০২৫ অথবা 2024-12-25 তারিখে।"
dates = extract_bengali_dates(text)
print(f"Dates found: {dates}")

# Expected Output:
# Dates found: ['১৫ জানুয়ারি, ২০২৫', '2024-12-25']
```

---

### 3. `extract_numbers(text)`

*   **Description:** Finds standalone numerical values (integers or floating-point numbers) within the text. It supports both Bengali and English digits, allows for commas as thousands separators (e.g., `১,০০০`), decimal points (`.`), and optional leading negative signs (`-` or `−`). It's designed to run *after* more specific extractors (like dates, times, phones) in a full normalization pipeline to avoid incorrectly matching parts of those structures.
*   **Supported Formats (Examples):** `১০০`, `45`, `২.৫`, `-১০.৭৫`, `১,২৩,৪৫৬`, `98.6`, `−5`
*   **Returns:** `list[str]` - A list of matched number strings.

```python
from bengali_normalizer.extractor import extract_numbers

text = "সংখ্যাগুলো হলো ১২৩, -৭৫.৫ এবং ১,০০,০০০।"
# Note: If text contained dates/times, this extractor might pick up
# number parts if not run in the correct sequence.
numbers = extract_numbers(text)
print(f"Numbers found: {numbers}")

# Expected Output:
# Numbers found: ['১২৩', '-৭৫.৫', '১,০০,০০০']
```

---

### 4. `extract_time(text)`

*   **Description:** Extracts time expressions in HH:MM or HH:MM:SS format. It supports Bengali and English digits, optional AM/PM markers (case-insensitive, with or without dots, e.g., `AM`, `pm`, `A.M.`, `পি.এম.`), and an optional trailing "টায়".
*   **Supported Formats (Examples):** `১০:০০ AM`, `১৯:৪৫:০০`, `৯:৩০ মিনিটে` (extracts `৯:৩০`), `3:45 PM`, `১২:০০ PM টায়`, `8:00 P.M.`
*   **Returns:** `list[str]` - A list of matched time expression strings.

```python
from bengali_normalizer.extractor import extract_time

text = "সকাল ১০:৩০ টায় এবং রাত 21:00:15 তে দেখা হবে।"
times = extract_time(text)
print(f"Times found: {times}")

# Expected Output:
# Times found: ['১০:৩০ টায়', '21:00:15']
```

---

### 5. `extract_taka_amounts(text)`

*   **Description:** Finds expressions representing Bangladeshi Taka currency amounts. It looks for patterns starting with the Taka symbol (`৳`), or numbers followed by the words "টাকা" or "টাকার". It handles commas, decimal points, and potentially units like "লক্ষ" or "কোটি" when used with the symbol.
*   **Supported Formats (Examples):** `৳৫০০`, `২৫০ টাকা`, `১০ টাকার`, `৳১,২৩,৪৫৬.৭৮`, `৳১০ লক্ষ টাকা`, `৳ ২৫০`
*   **Returns:** `list[str]` - A list of matched Taka amount strings.

```python
from bengali_normalizer.extractor import extract_taka_amounts

text = "খরচ ৳৫০০.৫০ এবং লাভ ২৫,০০০ টাকা।"
amounts = extract_taka_amounts(text)
print(f"Taka amounts found: {amounts}")

# Expected Output:
# Taka amounts found: ['৳৫০০.৫০', '২৫,০০০ টাকা']
```

---

### 6. `extract_percentages(text)`

*   **Description:** Detects percentage values, looking for numbers (integers or decimals, Bengali/English digits, optional negative sign) followed by either the percent symbol (`%`) or the Bengali word "শতাংশ". Allows for optional space between the number and the symbol/word.
*   **Supported Formats (Examples):** `২০%`, `১৫.৫ শতাংশ`, `75.5 %`, `-১০শতাংশ`, `৯৯.৯%`
*   **Returns:** `list[str]` - A list of matched percentage strings (including the number and the %/শতাংশ part).

```python
from bengali_normalizer.extractor import extract_percentages

text = "ডিসকাউন্ট ছিল ১৫% এবং বৃদ্ধি -২.৫ শতাংশ।"
percentages = extract_percentages(text)
print(f"Percentages found: {percentages}")

# Expected Output:
# Percentages found: ['১৫%', '-২.৫ শতাংশ']
```

---

### 7. `extract_temperatures(text)`

*   **Description:** Finds temperature readings. It looks for numbers (integers/decimals, Bengali/English, optional negative sign) followed by common temperature units or symbols like `°C`, `°F`, `°K`, `ডিগ্রি`, `সেলসিয়াস`, `ফারেনহাইট`, `সে.` (abbreviation for Celsius). Case-insensitive for C/F/K.
*   **Supported Formats (Examples):** `৩৫°C`, `৩২.৫ ডিগ্রি সেলসিয়াস`, `98.6°F`, `-৫° সে.`, `৪০ ডিগ্রি`, `100 C`
*   **Returns:** `list[str]` - A list of matched temperature strings.

```python
from bengali_normalizer.extractor import extract_temperatures

text = "তাপমাত্রা ছিল ৩০.৫°C অথবা প্রায় 87°F।"
temperatures = extract_temperatures(text)
print(f"Temperatures found: {temperatures}")

# Expected Output:
# Temperatures found: ['৩০.৫°C', '87°F']
```

---

### 8. `extract_ratios(text)`

*   **Description:** Detects expressions representing ratios. It looks for numbers separated by colons (`:`), Bengali visarga (`ঃ`), or hyphens (`-`). It also finds patterns like "X থেকে Y" and "X অনুপাত Y". Numbers can include decimals and commas. Optionally matches trailing words like "অনুপাতে" or "রেশিওতে".
*   **Supported Formats (Examples):** `১:৩`, `৫:৩:১`, `২.৫:১`, `১ঃ১০০`, `৭-৩`, `১ থেকে ৫`, `১ অনুপাত ৫`, `২:১ অনুপাতে`
*   **Returns:** `list[str]` - A list of matched ratio expression strings.

```python
from bengali_normalizer.extractor import extract_ratios

text = "অনুপাত ২:৩ এবং সংখ্যা ১ থেকে ১০ এর মধ্যে।"
ratios = extract_ratios(text)
print(f"Ratios found: {ratios}")

# Expected Output:
# Ratios found: ['২:৩', '১ থেকে ১০']
```

---

### 9. `extract_ordinals(text)`

*   **Description:** Finds ordinal numbers, which indicate position or rank. It detects numbers (allowing commas) followed by common Bengali ordinal suffixes (`ম`, `য়`, `লা`, `রা`, `শে`, `ই`, `র্থ`, `তম`) or English suffixes (`st`, `nd`, `rd`, `th`).
*   **Supported Formats (Examples):** `১ম`, `২য়`, `3rd`, `৪র্থ`, `১০ম`, `১লা`, `৩রা`, `২২শে`, `10,000তম`, `21st`
*   **Returns:** `list[str]` - A list of matched ordinal number strings.

```python
from bengali_normalizer.extractor import extract_ordinals

text = "সে ছিল ১ম এবং আমি ৩য়। আজ ১লা বৈশাখ।"
ordinals = extract_ordinals(text)
print(f"Ordinals found: {ordinals}")

# Expected Output:
# Ordinals found: ['১ম', '৩য়', '১লা']
```

---

### 10. `extract_years_with_context(text)`

*   **Description:** Specifically looks for 4-digit numbers that likely represent years, giving priority to those appearing immediately before or after context words like "সাল", "সালের", or "সন". It helps distinguish years from other 4-digit numbers. Supports Bengali and English digits for the year.
*   **Supported Formats (Examples):** `২০২৫ সাল`, `সাল ১৯৭১`, `১৯৪৫ সন`, `২০২৩ সালের`
*   **Returns:** `list[str]` - A list of matched year strings, including the context word if found (e.g., "২০২৫ সাল").

```python
from bengali_normalizer.extractor import extract_years_with_context

text = "মুক্তিযুদ্ধ ১৯৭১ সালে হয়েছিল। নতুন পরিকল্পনা ২০২৫ সালের।"
years = extract_years_with_context(text)
print(f"Years with context found: {years}")

# Expected Output:
# Years with context found: ['১৯৭১ সালে', '২০২৫ সালের']
```

---


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

# Bengali Normalizer Utilities

This document describes the utility functions found within the `bengali_normalizer.utils` module. These functions provide essential low-level operations like digit conversion, date/time parsing, string manipulation, and phonetic conversion, primarily supporting the main normalization pipeline (`normalizer.py` and `methods.py`).

While these functions are mostly intended for internal use, they can be imported and used directly for specific tasks if needed.

**Note:** Many of these functions depend on data structures (like number-to-word mappings, month names) defined in `bengali_normalizer.conversion_data`. Ensure this module is present and correctly populated for the utilities to function as expected.

## Importing Utilities

To use these functions directly, import them from the `utils` submodule:

```python
from bengali_normalizer.utils import bangla_to_english_number, remove_extra_spaces
# Import other functions as needed
```

---

## Function Descriptions and Examples

### 1. `separate_year(year_str)`

*   **Description:** Takes a 4-digit year as a string (accepts both Bengali '০-৯' and Western '0-9' digits). It converts the year to an integer and separates it into two parts: the century/millennium part (e.g., 1900, 2000) and the remaining two digits (e.g., 95, 23). Useful for converting years into words like "উনিশশো পঁচানব্বই". Returns a tuple `(part1_int, part2_int)`. Returns `(None, None)` if parsing fails.
*   **Parameters:**
    *   `year_str` (str): A string representing a 4-digit year.
*   **Returns:** `tuple[Optional[int], Optional[int]]`

```python
from bengali_normalizer.utils import separate_year

year1_bn = "১৯৯৮"
year2_en = "2025"
invalid_year = "abc"

parts1 = separate_year(year1_bn)
parts2 = separate_year(year2_en)
parts3 = separate_year(invalid_year) # Example of failure

print(f"'{year1_bn}' -> {parts1}")
print(f"'{year2_en}' -> {parts2}")
print(f"'{invalid_year}' -> {parts3}")

# Expected Output:
# '১৯৯৮' -> (1900, 98)
# '2025' -> (2000, 25)
# Warning: Could not parse year 'abc' as integer. (Printed to stderr)
# 'abc' -> (None, None)
```

---

### 2. `extract_date_components_bangla(date_str)`

*   **Description:** Parses a date string provided in various common Bengali or English formats (e.g., `১৫ জানুয়ারি, ২০২৫`, `05-05-1995`, `২২/মার্চ/২০২৫`). It cleans the input (removes ordinal suffixes, normalizes separators), translates month names and digits for parsing using `dateutil.parser`, and then converts the extracted day, month name, and year back into Bengali strings.
*   **Dependencies:** Requires `dateutil.parser` library and relies on `conversion_data.bangla_months` map.
*   **Parameters:**
    *   `date_str` (str): The date string to parse.
*   **Returns:** `tuple[Optional[str], Optional[str], Optional[str]]` - A tuple containing (day\_bengali, month\_bengali, year\_bengali). Returns `(None, None, None)` if parsing fails.

```python
from bengali_normalizer.utils import extract_date_components_bangla

date1 = "১৫ জানুয়ারি, ২০২৫"
date2 = "05-05-1995"
date3 = "২২শে মার্চ, ২০২৪" # Handles common suffixes
invalid_date = "32শে জানুয়ারি"

components1 = extract_date_components_bangla(date1)
components2 = extract_date_components_bangla(date2)
components3 = extract_date_components_bangla(date3)
components4 = extract_date_components_bangla(invalid_date) # Example of failure

print(f"'{date1}' -> {components1}")
print(f"'{date2}' -> {components2}")
print(f"'{date3}' -> {components3}")
print(f"'{invalid_date}' -> {components4}")

# Expected Output:
# '১৫ জানুয়ারি, ২০২৫' -> ('১৫', 'জানুয়ারি', '২০২৫')
# '05-05-1995' -> ('৫', 'মে', '১৯৯৫')
# '২২শে মার্চ, ২০২৪' -> ('২২', 'মার্চ', '২০২৪')
# Error parsing date '32শে জানুয়ারি'... (Printed to stderr)
# '32শে জানুয়ারি' -> (None, None, None)
```

---

### 3. `bangla_to_english_number(input_number_str)`

*   **Description:** Converts a number represented as a string, which can contain Bengali ('০-৯') or Western ('0-9') digits, along with optional commas (`,`), a decimal point (`.`), and negative signs (`-` or `−`), into a standard Python `int` or `float`. It handles cleaning (removing commas, normalizing negative signs) and digit translation before conversion.
*   **Parameters:**
    *   `input_number_str` (str): The string representation of the number.
*   **Returns:** `Union[int, float, None]` - The converted number, or `None` if the conversion fails.

```python
from bengali_normalizer.utils import bangla_to_english_number

num_str1 = "১২৩.৪৫"
num_str2 = "-১,০০০"
num_str3 = "−৭৫"
num_str4 = "৫০%" # Example likely to fail conversion as it's not purely a number

num1 = bangla_to_english_number(num_str1)
num2 = bangla_to_english_number(num_str2)
num3 = bangla_to_english_number(num_str3)
num4 = bangla_to_english_number(num_str4)

print(f"'{num_str1}' -> {num1} (Type: {type(num1).__name__})")
print(f"'{num_str2}' -> {num2} (Type: {type(num2).__name__})")
print(f"'{num_str3}' -> {num3} (Type: {type(num3).__name__})")
print(f"'{num_str4}' -> {num4}")

# Expected Output:
# '১২৩.৪৫' -> 123.45 (Type: float)
# '-১,০০০' -> -1000 (Type: int)
# '−৭৫' -> -75 (Type: int)
# Warning: Could not convert '৫০%' to English number. (Printed to stderr)
# '৫০%' -> None
```

---

### 4. `remove_extra_spaces(input_text)`

*   **Description:** A simple string cleaning utility. It takes an input string and replaces any sequence of two or more whitespace characters (including spaces, tabs, newlines) with a single space. It also removes leading and trailing whitespace from the string.
*   **Parameters:**
    *   `input_text` (str): The text to clean.
*   **Returns:** `str` - The cleaned text with normalized spacing.

```python
from bengali_normalizer.utils import remove_extra_spaces

text = "   অনেক   \n  স্পেস  এবং \tট্যাব   "
cleaned_text = remove_extra_spaces(text)

print(f"Original: '{text}'")
print(f"Cleaned: '{cleaned_text}'")

# Expected Output:
# Original: '   অনেক   \n  স্পেস  এবং \tট্যাব   '
# Cleaned: 'অনেক স্পেস এবং ট্যাব'
```

---

### 5. `convert_decimal_to_words(decimal_part_str)`

*   **Description:** Specifically designed to handle the *decimal part* of a number (the digits after the decimal point). It takes these digits as a string, ensures they are Bengali digits, and then converts *each digit individually* into its corresponding Bengali word using the `conversion_data.banglaNum` mapping. Returns a space-separated string of these digit words.
*   **Dependencies:** Relies on `conversion_data.banglaNum`.
*   **Parameters:**
    *   `decimal_part_str` (str): A string containing only the digits found after the decimal point.
*   **Returns:** `str` - Space-separated Bengali words for each digit.

```python
# Assuming conversion_data.banglaNum = {'০': 'শূন্য', '১': 'এক', ... '৫': 'পাঁচ', ...}
from bengali_normalizer.utils import convert_decimal_to_words

decimal1 = "৭৫"
decimal2 = "০৫"
decimal3 = ""

words1 = convert_decimal_to_words(decimal1)
words2 = convert_decimal_to_words(decimal2)
words3 = convert_decimal_to_words(decimal3)

print(f"'{decimal1}' -> '{words1}'")
print(f"'{decimal2}' -> '{words2}'")
print(f"'{decimal3}' -> '{words3}'")

# Expected Output:
# '৭৫' -> 'সাত পাঁচ'
# '০৫' -> 'শূন্য পাঁচ'
```

---

### 6. `get_bangla_time_period(hour_24)`

*   **Description:** Determines the appropriate Bengali time period word (like "ভোর", "সকাল", "দুপুর", "বিকেল", "সন্ধ্যা", "রাত") based on the hour provided in 24-hour format (0-23).
*   **Parameters:**
    *   `hour_24` (int): The hour (0-23).
*   **Returns:** `str` - The corresponding Bengali time period word, or an empty string/warning for invalid input.

```python
from bengali_normalizer.utils import get_bangla_time_period

hour1 = 5  # ভোর
hour2 = 11 # সকাল
hour3 = 14 # দুপুর
hour4 = 17 # বিকেল
hour5 = 19 # সন্ধ্যা
hour6 = 23 # রাত
hour7 = 1  # রাত

period1 = get_bangla_time_period(hour1)
period2 = get_bangla_time_period(hour2)
period3 = get_bangla_time_period(hour3)
period4 = get_bangla_time_period(hour4)
period5 = get_bangla_time_period(hour5)
period6 = get_bangla_time_period(hour6)
period7 = get_bangla_time_period(hour7)

print(f"{hour1} -> {period1}")
print(f"{hour2} -> {period2}")
print(f"{hour3} -> {period3}")
print(f"{hour4} -> {period4}")
print(f"{hour5} -> {period5}")
print(f"{hour6} -> {period6}")
print(f"{hour7} -> {period7}")

# Expected Output:
# 5 -> ভোর
# 11 -> সকাল
# 14 -> দুপুর
# 17 -> বিকেল
# 19 -> সন্ধ্যা
# 23 -> রাত
# 1 -> রাত
```

---

### 7. `bangla_to_ipa_converter(sentence)`

*   **Description:** Attempts a rule-based conversion of a Bengali text string into the International Phonetic Alphabet (IPA). It iterates through the input string, trying to match the longest possible character sequences (especially conjuncts/যুক্তাক্ষর) against predefined mappings in `conversion_data.bangla_conjuncts_to_ipa`. If no conjunct matches, it falls back to mappings for individual characters in `conversion_data.bangla_to_ipa`.
*   **Dependencies:** Accuracy is highly dependent on the completeness and correctness of the `bangla_to_ipa` and `bangla_conjuncts_to_ipa` dictionaries in `conversion_data.py`.
*   **Limitations:** This is a basic, rule-based approach and may not capture all phonetic nuances, variations in pronunciation, or context-dependent sound changes present in spoken Bengali.
*   **Parameters:**
    *   `sentence` (str): The Bengali text to convert.
*   **Returns:** `str` - The attempted IPA representation of the input string. Characters or sequences not found in the mappings will typically be passed through unchanged.

```python
# This example assumes hypothetical mappings in conversion_data.py
# from bengali_normalizer.conversion_data import bangla_to_ipa, bangla_conjuncts_to_ipa
# bangla_to_ipa = {'ব': 'b', 'া': 'ɑ', 'ং': 'ŋ', 'ল': 'l'}
# bangla_conjuncts_to_ipa = {} # Assuming no specific conjunct map for simplicity here

from bengali_normalizer.utils import bangla_to_ipa_converter

text = "বাংলা"

# Run the converter (Make sure conversion_data has some mappings)
ipa_text = bangla_to_ipa_converter(text)

print(f"'{text}' -> '{ipa_text}'")

# Example Expected Output (highly dependent on actual maps):
# 'বাংলা' -> 'bɑŋlɑ'
```

---

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
