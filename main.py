from stats import *

def main():
    PATH = get_path(sys.argv)
    
    content = get_book_text(PATH)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    
    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_count(content)
    sort_counts = sort_dict(char_counts)
         
    for map in sort_counts:
        if map["char"].isalpha():
            print(f"{map["char"]}: {map["num"]}")

    print("============= END ===============")

main()
    
