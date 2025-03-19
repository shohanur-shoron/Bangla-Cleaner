from utills import *
from number_in_word import *
from exteactor import *
from datetime import datetime


def date_to_word(date):
    day, month, year = extract_date_components_bangla(date)
    word = ''
    first_half, second_half = separate_year(year)
    if first_half%1000 == 0:
        num = first_half//1000
        word = englishNum[num] + " " + thousand
    else:
        num = first_half//100
        word = englishNum[num] + hundred_suffix
        
    if second_half != 0:
        word = word + " " + englishNum[second_half]
    
    word = day_name[day] + " " + month + " " + word
    return word


def convert_integer_to_words(number):
    if number == 0:
        return "শূন্য"

    word = ""
    if number >= 10 ** 7:  # কোটি
        crore_part = number // 10 ** 7
        word += convert_integer_to_words(crore_part) + " " + "কোটি"
        number %= 10 ** 7
    if number >= 10 ** 5:  # লক্ষ
        lakh_part = number // 10 ** 5
        word += " " + convert_integer_to_words(lakh_part) + " " + "লক্ষ"
        number %= 10 ** 5
    if number >= 10 ** 3:  # হাজার
        thousand_part = number // 10 ** 3
        word += " " + convert_integer_to_words(thousand_part) + " " + "হাজার"
        number %= 10 ** 3
    if number >= 100:  # শত
        hundred_part = number // 100
        word += " " + englishNum[hundred_part] + "শো"
        number %= 100
    if number > 0:  # Remaining less than 100
        word += " " + englishNum[number]

    return word



