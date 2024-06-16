def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    char_count = count_char(text) 
    sorted_list = report(char_count)
    
    # Print report below
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document")
    print()

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")

    print(f"--- End report ---")

def sort_on(item):
    return item["num"]

def report(count):
    new_char_list = []
    
    # Convert the dict into a list of dicts

    for char in count:
            new_char_list.append({"char": char, "num": count[char]})

    new_char_list.sort(reverse=True, key=sort_on)

    return new_char_list

def count_char(text):
    char_found = {}
    lower_case_text = text.lower()

    for chars in lower_case_text:
        if chars in char_found:
            char_found[chars] += 1
        else:
            char_found[chars] = 1

    return char_found

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)

main()
