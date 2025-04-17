from random import choice
from string import ascii_letters, digits, punctuation

def creating_password(length_of_password=11, if_special_character_allowed="Yes"):
    character = digits + ascii_letters 
    if if_special_character_allowed == "Yes":
        character = character + punctuation
    return "".join(choice(character) for every_character in range(int(length_of_password)))