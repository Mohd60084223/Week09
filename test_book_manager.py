simport unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("123", "Book One", "Author A")
        self.book2 = Book("456", "Book Two", "Author B")

    def test_add_and_list_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_books(),[self.book1, self.book2])


    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book('Book One')
        self.assertEqual(self.manager.list_books(),[])

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book('Nonexistent Book')
        self.assertEqual(self.manager.list_books(), [ self.book1])
        

if __name__ == '__main__':
    unittest.main()
