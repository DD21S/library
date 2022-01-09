from django.test import TestCase

from library.models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name="My Name is F",
            author="Steve Gates",
        )

    def test_book_create(self):
        self.assertEqual(self.book.name, "My Name is F")
        self.assertEqual(self.book.author, "Steve Gates")

    def test_book_no_read(self):
        self.assertEqual(self.book.is_read, False)

    def test_book_is_read(self):
        self.book.is_read = True

        self.assertEqual(self.book.is_read, True)
