def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    char_counts  = character_counts(text)
    alpha_counts = []
    for c,v in char_counts.items():
       if c.isalpha():
           alpha_counts.append({"char":c, "count":v})
    alpha_counts.sort(reverse=True, key=sort_on)    
    
    
    print(f"--- Begin report of {book_path} ---")
    print (f"This book contains {num_words} words.\n")

    for c in range(len(alpha_counts)):
     print(f"The '{alpha_counts[c]["char"]}' character was found {alpha_counts[c]["count"]} times.")
    print()
    print("--- END OF REPORT ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["count"]

def character_counts(text):
    characters = {}
    lower_string = text.lower()
    for w in lower_string:
        if w in characters:
            characters[w] = characters[w] + 1
        else:
            characters[w] = 1
    return characters
    

main()