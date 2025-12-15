from stats import get_book_text, count_book_words, count_chars, sort_chars
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_name = sys.argv[1]

    content = get_book_text(book_name)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_name}")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(content)} total words")
    print("--------- Character Count -------")
    for char in sort_chars(count_chars(content)):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

  
main()
