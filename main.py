from stats import count_words, get_char_counts, get_sorted_char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_counts(text)
    print(char_counts)
    sorted_chars = get_sorted_char_counts(char_counts)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============ END =============")

main()

