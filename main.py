def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    char_occurences = get_char_occurences(text)
    get_report(char_occurences, num_words, book_path)

def get_number_of_words(text):
    return len(text.split())

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
      return f.read()

def get_char_occurences(text):
    char_dict = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch in char_dict:
                char_dict[ch] += 1
            else:
                char_dict[ch] = 1
    return char_dict

def get_report(char_dict, num_words, book_path):
    list_of_tuples = []

    for char in char_dict:
        char_tuple = (char_dict[char], char)
        list_of_tuples.append(char_tuple)
    list_of_tuples.sort(reverse=True)
    

    print(book_path)
    print(f"Number of words: {num_words}")
    for tp in list_of_tuples:
        print(f"The letter {tp[1]} was found {tp[0]} times")

main()