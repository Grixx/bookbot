def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    char_counts  = character_counts(text)
    print(char_counts)

    print(f"--- Begin report of {book_path}")
    print (f"This book contains {num_words} words")

    



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):    
    with open(path) as f:
        return f.read()

def character_counts(text):
    characters = {}
    for w in lower_string:
        lower_string = text.lower()
        if w in characters:
            characters[w] = characters[w] + 1
        else:
            characters[w] = 1
    return characters
    

main()