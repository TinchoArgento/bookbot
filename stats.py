import sys

def get_book_text(): #this get the book from the second argument of the command to run the app
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def word_counter():
    count = 0
    separate_words = get_book_text().split()
    for word in separate_words:
        count += 1
    return count

def letter_counter(): #creates a list of dictionaries
    quantity_by_letter = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
        "æ":0,
        "â":0,
        "ê":0,
        "ë":0,
        "ô":0,
        }
    low_case_words = get_book_text().lower()
    for letter in low_case_words:
        if letter in quantity_by_letter:
            quantity_by_letter[letter] += 1
    return quantity_by_letter

def get_num(x): #helper function necesary to get the number value in create_list()
    return x["num"]

def create_list():#returns a list of dictonaries sorted by number
    old_dict = letter_counter()
    lista = []
    for key in old_dict:
        new_dict = {"char":key,"num":old_dict[key]}
        lista.append(new_dict)
    lista.sort(reverse=True, key=get_num)
    return lista


