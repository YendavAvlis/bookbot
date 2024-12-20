
def count_words(book):
    book = book.split()
    count = 0
    for word in book:
        count += 1
    return count

def count_letters(book):
    count_letters = {}
    words = book.split()
    
    for letter in words:
        characters = letter.lower()
        for char in characters:
            if char.isalpha():
                if char in count_letters:
                    count_letters[char] += 1
                else:
                    count_letters[char] = 1
    return count_letters


try:
    book_name = input("Enter book name: ")
    with open(f"books/{book_name.lower()}.txt") as f:
        content = f.read()
    
    sorted_values = dict(sorted(count_letters(content).items(), key= lambda item: item[1], reverse=True ))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(content)} words found in the document\n")

    for k, v in sorted_values.items():
        print(f"The '{k}' character was found {v}")
            
    print("\n--- End report ---")

except FileNotFoundError:
    if book_name == "":
        print('Please, type the name of the book')
    else:
        print(f" The file {book_name}.txt does not exist")


