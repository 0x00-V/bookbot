import sys
from stats import *
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_count = char_count(text)
    sorted_chars = sorting_algo(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        char = i["char"]
        count = i["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()
