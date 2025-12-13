from stats import get_book_text, count_book_words, count_chars, sort_chars

def main():
    content = get_book_text("books/frankenstein.txt")
    print(f"Found {count_book_words(content)} total words")
    book_chars_count = count_chars(content)
    print(sort_chars(book_chars_count))

main()
