import sys

def get_path(lst: list):
    if len(lst) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return lst[1]

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()
    return content

def get_num_words(content: str):
    text = content.split()
    return len(text)

def get_char_count(content: str):
    char_count_map = {}
    content = content.lower()
    
    for c in content:
        char_count_map[c] = char_count_map.get(c,0) + 1

    return char_count_map

def sort_on(data):
    return data["num"]

def sort_dict(data: dict):
    lst = []
    for key, value in data.items():
        tmp = {
            "char": key,
            "num": value
        }

        lst.append(tmp)
    
    lst.sort(reverse=True, key=sort_on)
    return lst            
