import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        # Initial setup for test books
        self.book1 = Book("ISBN001", "The Great Gatsby", "F. Scott Fitzgerald")
        self.book2 = Book("ISBN002", "To Kill a Mockingbird", "Harper Lee")
        self.book3 = Book("ISBN003", "1984", "George Orwell")

    def test_add_book(self):
        """Test adding books to the manager."""
        self.manager.add_book(self.book1)
        self.assertIn(self.book1, self.manager.books, "Book1 should be added to the manager.")

        # Add another book and test
        self.manager.add_book(self.book2)
        self.assertIn(self.book2, self.manager.books, "Book2 should be added to the manager.")

    def test_prevent_duplicate_isbn(self):
        """Ensure books with duplicate ISBNs are not added."""
        self.manager.add_book(self.book1)
        # Attempt to add a book with an existing ISBN
        duplicate_book = Book("ISBN001", "The Great Gatsby Duplicate", "F. Scott Fitzgerald")
        self.manager.add_book(duplicate_book)
        # There should only be one instance of book with ISBN001
        self.assertTrue(self.manager.books.count(self.book1) == 1, "Duplicate ISBN book should not be added.")

    def test_remove_book(self):
        """Test removing books by ISBN."""
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        # Remove a book and test
        self.manager.remove_book("ISBN001")
        self.assertNotIn(self.book1, self.manager.books, "Book1 should be removed from the manager.")

    def test_list_books(self):
        """Test listing all books."""
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.manager.add_book(self.book3)
        expected_books = [self.book1, self.book2, self.book3]
        actual_books = self.manager.list_books()
        self.assertListEqual(actual_books, expected_books, "The list of books should match the books added to the manager.")

if __name__ == '__main__':
    unittest.main()
