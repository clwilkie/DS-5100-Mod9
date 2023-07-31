import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        self.assertTrue('Foundation' in list(book_obj.book_list['book_name']))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        book_obj.add_book('Foundation',5)
        expected = 1
        self.assertEqual(len(book_obj.book_list['book_name']),expected)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        self.assertTrue(book_obj.has_read('Foundation'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        self.assertFalse(book_obj.has_read('I, Robot'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        book_obj.add_book('War of the Worlds',4)
        book_obj.add_book('Dune',5)
        expected = 3
        self.assertEqual(book_obj.num_books_read(),expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_obj = BookLover('Colin','exd4er@virginia.edu','Sci-Fi')
        book_obj.add_book('Foundation',5)
        book_obj.add_book('War of the Worlds',3)
        book_obj.add_book('Dune',5)
        expected = 2
        self.assertEqual(len(book_obj.fav_books()),expected)
                
if __name__ == '__main__':
    unittest.main(verbosity=3)