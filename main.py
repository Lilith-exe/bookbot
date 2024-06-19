def main():
    path = "books/frankenstein.txt"
    book_string = book_text(path)
    num_words = word_count(book_string)
    char_count = character_count(book_string)
    print(f"There are {num_words} words in this book!")
    print(char_count)

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
    

main()