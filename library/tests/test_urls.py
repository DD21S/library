from django.test import TestCase
from django.urls import resolve, reverse

from library import views

class BookUrlsTest(TestCase):
    def test_books_url_resolves(self):
        url = reverse('library:books')
        self.assertEquals(
            resolve(url).func.view_class,
            views.BookListView
        )

    def test_book_update_no_post_resolves(self):
        url = reverse('library:update_book', args=[1])
        self.assertEquals(
            resolve(url).func,
            views.book_update_view
        )
