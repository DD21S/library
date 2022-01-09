from django.test import TestCase, Client
from django.urls import reverse

from library.models import Book

class LibraryViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            name="My Name is F",
            author="Steve Gates",
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('library:books'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/list.html')
        self.assertContains(response, self.book.name)

    def test_book_create_no_post_view(self):
        response = self.client.get(reverse('library:create_book'))

        self.assertRedirects(response, '/')

    def test_book_create_post_view(self):
        response = self.client.post(
            reverse('library:create_book'), 
            {
                'name': 'Yo no',
                'author': 'Taika Waititi',
                'action': 'create' 
            }
        )

        self.assertRedirects(response, '/')

    def test_book_is_read_view(self):
        response = self.client.get(
            reverse('library:is_read_book', args=[self.book.id])
        )

        self.assertRedirects(response, '/')

    def test_book_update_no_post_view(self):
        response = self.client.get(
            reverse('library:update_book', args=[self.book.id])
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/update.html')
        self.assertContains(response, self.book.name)

    def test_book_update_view(self):
        response = self.client.post(
            reverse('library:update_book', args=[self.book.id]),
            {
                'name': 'Hola Mundo',
                'author': 'Hello World',
                'action': 'update'
            }
        )

        self.assertRedirects(response, '/')       

    def test_book_delete_view(self):
        response = self.client.post(
            reverse('library:delete_book', args=[self.book.id])
        )

        self.assertRedirects(response, '/')
