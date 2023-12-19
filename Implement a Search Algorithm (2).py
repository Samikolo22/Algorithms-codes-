# -*- coding: utf-8 -*-

sample_books = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "isbn": "978-0-316-76948-0", "publisher": "Little, Brown and Company"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "isbn": "978-0-06-112008-4", "publisher": "J.B. Lippincott & Co."},
    {"title": "1984", "author": "George Orwell", "year": 1949, "isbn": "978-0-452-28423-4", "publisher": "Secker & Warburg"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "isbn": "978-0-7432-7356-5", "publisher": "Scribner"},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967, "isbn": "978-0-06-112008-4", "publisher": "Harper & Row"},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "isbn": "978-0-06-085052-4", "publisher": "Chatto & Windus"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "isbn": "978-0-618-00221-4", "publisher": "George Allen & Unwin"},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997, "isbn": "978-0-7475-3269-6", "publisher": "Bloomsbury"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "isbn": "978-0-261-10238-3", "publisher": "Allen & Unwin"},
    {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "isbn": "978-0-14-243724-7", "publisher": "Harper & Brothers"}
]

def binary_search_by_title(books, title):
    low, high = 0, len(books) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = books[mid]['title']

        if mid_title == title:
            return mid
        elif mid_title < title:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def partial_match_search(books, partial_title):
    matches = []
    for i, book in enumerate(books):
        if partial_title.lower() in book['title'].lower():
            matches.append(i)
    return matches

def universal_search(books, search_term):
    matches = []
    for i, book in enumerate(books):
        if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
            matches.append(i)
    return matches

title_to_search = "The Catcher in the Rye"
index = binary_search_by_title(sample_books, title_to_search)
print(f"Book with title '{title_to_search}' found at index {index}" if index != -1 else f"Book with title '{title_to_search}' not found")

partial_title_to_search = "The"
partial_matches = partial_match_search(sample_books, partial_title_to_search)
print(f"Books with partial title '{partial_title_to_search}': {partial_matches}")

universal_search_term = "J.D. Salinger"
universal_matches = universal_search(sample_books, universal_search_term)
print(f"Books with title or author '{universal_search_term}': {universal_matches}")
