# MAIN FUNCTION TO ENTER PROGRAM
def main():
    book_path = "books/frankenstein.txt"

    # READ BOOK INTO PROGRAM AND SAVE IT IN file_contents
    with open(book_path) as f:
        file_contents = f.read()

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(file_contents)} words found in the document")

    # CREATE HASHMAP OF INDIVIDUAL CHARACTERS WITHIN THE BOOK AND THEIR RESPECTIVE COUNTS
    chars = char_count(file_contents)

    # CREATE AN EMPTY ARRAY TO BE LOOPED THROUGH IN ORDER TO PRINT CHARACTERS AND THEIR COUNTS IN DESCENDING ORDER
    chars_list = []

    # POPULATE CHARACTER ARRAY 
    for char in chars:
        chars_list.append(char)

    # SORT THE CHARACTER ARRAY INTO DESCENDING ORDER
    chars_list.sort()
    print(chars_list)

    # PRINT THE CHARACTERS AND THEIR COUNT
    # FIRST CHECK WHETHER CHARACTER IS AN ALPHABETIC LETTER
    for char in chars_list:
        if char.isalpha():
            print(f"The \'{char}\' character was found {chars[char]} times")

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


# RUN PROGRAM
main()