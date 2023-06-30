# MAIN FUNCTION TO ENTER PROGRAM
def main():
    book_path = "books/frankenstein.txt"

    # READ BOOK INTO PROGRAM AND SAVE IT IN file_contents
    with open(book_path) as f:
        file_contents = f.read()

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")

    # CREATE HASHMAP OF INDIVIDUAL CHARACTERS WITHIN THE BOOK AND THEIR RESPECTIVE NUMBER OF OCCURRENCES
    chars = char_count(file_contents)

    # CREATE AN ARRAY OF CHARACTERS ARRANGED IN DESCENDING ORDER BY THEIR NUMBER OF OCCURRENCES
    chars_list = dict_into_sorted_list(chars)

    # PRINT THE CHARACTERS AND THEIR COUNT
    # FIRST CHECK WHETHER CHARACTER IS AN ALPHABETIC LETTER
    # NB - Each iteration of the "char" variable is a dictionary whose key is the letter and val is the count
    for char in chars_list:
        if char['key'].isalpha():
            print(f"The \'{char['key']}\' character was found {char['val']} times")

    print("")
    print("--- End report ---")

# FUNCTIONS
def count_words(text):
    words = text.split()

    return len(words)

def char_count(text):
    chars = {}

    for char in text:
        char = char.lower()

        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def dict_into_sorted_list(dict):
    sorted_list = []

    for key in dict:
        sorted_list.append({"key": key, "val": dict[key]})
    
    sorted_list.sort(key=lambda x: x["val"], reverse=True)

    return sorted_list


# RUN PROGRAM
main()