import sys
from stats import get_book_text, count_words, count_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

try:
    book_text = get_book_text(book_path)
except FileNotFoundError:
    print(f"Error: File '{book_path}' not found.")
    sys.exit(1)

num_words = count_words(book_text)

char_counts = count_characters(book_text)

print("============ BOOKBOT ============")
print(f"Analyzing {book_path}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
print("Character counts (alphabetical only:)")
for char, count in sorted(char_counts.items()):
    print(f"'{char}: {count}'")
print("============= END ===============")
