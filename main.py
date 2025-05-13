from stats import get_book_text, count_words, count_characters

book_path = "books/frankenstein.txt"
book_text = get_book_text(book_path)
num_words = count_words(book_text)
char_counts = count_characters(book_text)

print(f"{num_words} words found in the document")
print("Character counts:")
print(char_counts)
