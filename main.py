from stats import word_count
from stats import char_count
from stats import sort_dict
import sys


def main():
    try:
        relative_path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(relative_path)
    words = get_book_text(relative_path)
    chars = get_book_text(relative_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    word_count(words)
    print("--------- Character Count -------")
    counted_chars = char_count(chars)
    sort_dict(counted_chars)

def get_book_text(filepath):
    with open(filepath) as frankenstein:
        return frankenstein.read()
        
main()