from stats import get_book_text, count_words, count_characters

book_path = "books/frankenstein.txt"
book_text = get_book_text(book_path)
num_words = count_words(book_text)
char_counts = count_characters(book_text)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
print("Character counts (alphabetical only:)")
for char, count in sorted(char_counts.items()):
    print(f"'{char}: {count}'")
print("============= END ===============")
