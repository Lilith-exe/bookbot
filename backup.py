def main():
    path = "books/frankenstein.txt"
    book_string = book_text(path)
    num_words = word_count(book_string)
    char_count = character_count(book_string)
    list = dict_list(char_count)
    sort_key = sort_on(dict)
    sorted_list = list_sort(list, sort_key)
    print(f"There are {num_words} words in this book!")
    print(sorted_list)
#    print(list_sort(char_count, sort_key))

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

#def dict_list(char_count):
#    list_chars = [{key: value} for key, value in char_count.items()]
#    return list_chars

def sort_on(dict):
    return dict["num"]

def list_sort(list, sort_key):
    sorted_list = list.sort(reverse = True, key = sort_key)
    return sorted_list

def dict_list(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            temp_dict = {"char": char, "num": char_count[char]}
            char_list.append(temp_dict)
    return char_list

    
    

main()