from stats import get_book_text, count_book_words, count_chars, sort_chars

def main():
    content = get_book_text("books/frankenstein.txt")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(content)} total words")
    print("--------- Character Count -------")
    for char in sort_chars(count_chars(content)):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

  
main()
