with open('books/frankenstein.txt') as f:
    content = f.read()

def count_words(book):
    book = book.split()
    count = 0
    for word in book:
        count += 1
    return f"The book contains {count} words!"

def count_letters(book):
    count_letters = {}

    for word in book:
        words = word.split()
        for letter in words:
            characters = letter.lower()
            if characters.isalpha():
                if characters in count_letters:
                    count_letters[characters] += 1
                else:
                    count_letters[characters] = 1
    return count_letters

print(count_words(content))
print(count_letters(content))

# print(count_letters)
# print(dir(count_letters))