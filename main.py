def main():
    path = "books/frankenstein.txt"
    book_string = book_text(path)
    num_words = word_count(book_string)
    char_count = character_count(book_string)
    char_list = dict_list(char_count)
    sorted_list = list_sort(char_list)
    print(f"There are {num_words} words in this book!")
    report(sorted_list)

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_string):
    words = book_string.split()
    return len(words)

def character_count(book_string):
    lowered_string = book_string.lower()
    character_dict = {}
    for character in lowered_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(item):
    return (item)["num"]

def list_sort(char_list):
    char_list.sort(reverse = True, key = sort_on)
    return char_list

def dict_list(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            temp_dict = {"char": char, "num": char_count[char]}
            char_list.append(temp_dict)
    return char_list

def report(sorted_list):
    print("--- Begin report ---")
    for letter in sorted_list:
        print(f"The '{letter['char']}' character was found {letter['num']} times")
    print("--- End report ---")
    
main()