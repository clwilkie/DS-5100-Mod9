import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self,book_name, book_rating):
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print('This book is already in your list!')
    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]