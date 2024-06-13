def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} of words found in the document")
    char_count = count_char(text) 
    pop_report = report(char_count)

def report(char_count):
    for char in char_count:
        print(f"The {char} character was found {char_count[char]} times")


def count_char(text):
    char_found = {}
    lower_case_text = text.lower()
    
    for char in lower_case_text:
        char_found[char] = 0
    for chars in lower_case_text:
        if chars in char_found:
            char_found[chars] += 1

    return char_found


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)

main()
