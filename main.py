import sys
from stats import words_counter, charachters_count, sorted_charachters_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(book_path):
    contents = ""
    with open(book_path) as f:
        contents = f.read()
    return contents


def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    total_words = words_counter(book)
    charachter_count_dictionary = charachters_count(book)
    sorted_chars_list = sorted_charachters_count(charachter_count_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_counter(book)} total words")
    print("--------- Character Count -------")
    # print(charachters_count(book))
    all_characters_list = sorted_chars_list
    for ch in all_characters_list:
        if ch["name"].isalpha():
            print(ch["name"] + ": " + str(ch["num"]))
    print("============= END ===============")


main()
