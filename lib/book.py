#!/usr/bin/env python3

class Book:
    def __init__(self, title = "title", author = "author", page_count = 0, genre = "genre"):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre
    
    def get_title(self):
        print('Retrieving title')
        return self._title

    def set_title(self, title):
        self._title = title

    title = property(get_title, set_title)

    def get_author(self):
        print('Retrieving author')
        return self._author

    def set_author(self, author):
        self._author = author

    author = property(get_author, set_author)

    def get_page_count(self):
        print('Retrieving page_count')
        return self._page_count

    def set_page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def get_genre(self):
        print('Retrieving genre')
        return self._genre

    def set_genre(self, genre):
        self._genre = genre

    genre = property(get_genre, set_genre)


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
