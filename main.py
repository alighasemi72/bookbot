from stats import words_counter, charachters_count


def get_book_text(book_path):
    contents = ""
    with open(book_path) as f:
        contents = f.read()
    return contents


def main():
    book = get_book_text("./books/frankenstein.txt")
    # print(book)
    print(f"Found {words_counter(book)} total words")
    print(charachters_count(book))


main()
