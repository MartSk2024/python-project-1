"""
projekt_1_py: první projekt do Engeto Online Python Akademie

author: Martin Soukenka
email: soukenka@post.cz
"""

import string

users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

username = input("username:")
password = input("password:")

is_registration = False
is_valid_text_number = False

for (key, value) in users.items():
    if key == username and value == password:
        print("-"*40)
        print(f"Welcome to the app, {username}!\nWe have 3 texts to be analyzed.")
        print("-"*40)
        is_registration = True
        break
else: 
    print("Unregistered user, terminating the program.")

if is_registration:
    text_number_input = input("Enter a number btw. 1 and 3 to select:")
    try:
        text_value = int(text_number_input)
        if text_value in range(1, len(TEXTS) + 1):
            is_valid_text_number = True
        else: 
            print("The entered number is out of range!")
            is_valid_text_number = False
    except ValueError:
        print("The entered input is not a number!")  

if is_valid_text_number: 
    word_count = 0
    number_count = 0
    word_title_count = 0
    word_upper_count = 0
    word_lower_count = 0
    sum_numbers = 0
    counter = {}
    text = TEXTS[text_value - 1].split()
    for word in text:
        word_parts = word.split("-")
        for part in word_parts: 
            if part.strip(string.punctuation).isalpha():
                word_count += 1
                if part.istitle():
                    word_title_count += 1 
                elif part.isupper(): 
                    word_upper_count += 1  
                elif part.islower():
                    word_lower_count += 1 
            elif part.strip(string.punctuation).isnumeric(): 
                word_count += 1
                number_count += 1
                sum_numbers = sum_numbers + int(part) 
            n = len(part.strip(string.punctuation))
            if n in counter:
                counter[n] += 1
            else: 
                counter[n] = 1    
    print("-"*40)
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {word_title_count} titlecase words.")
    print(f"There are {word_upper_count} uppercase words.")
    print(f"There are {word_lower_count} lowercase words.")
    print(f"There are {number_count} numeric strings.")
    print(f"The sum of all the numbers is {sum_numbers}.")
    print("-"*40)
    print("LEN|    OCCURENCES    |NR.")
    print("-"*40)
    counter_sorted = dict(sorted(counter.items()))
    max_length = max(counter_sorted.keys())
    max_digits = len(str(max_length))
    max_occurences = max(counter_sorted.values())
    for (length, count) in counter_sorted.items():
        print(f"{" "*(max_digits+1-len(str(length)))}{length}|" + \
            f"{"*"*(count)}{" "*(max_occurences+6-count)}|{count}")    
