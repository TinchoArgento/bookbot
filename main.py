import sys
from stats import letter_counter
from stats import word_counter
from stats import create_list

def main():
    call_arguments = sys.argv
    if len(call_arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter()} total words")
    print("--------- Character Count -------")
    for pair in create_list():
        if pair['char'].isalpha():
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")
    
main()    