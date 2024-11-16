with open('books/frankenstein.txt') as f:
    content = f.read()

def count_words(book):
    book = book.split()
    count = 0
    for word in book:
        count += 1
    return f"The book contains {count} words!"

print(count_words(content))