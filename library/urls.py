from django.urls import path

from library import views

app_name = 'library'

urlpatterns = [
    # ex: /
    path('', views.BookListView.as_view(), name='books'),
    path('create', views.book_create_view, name='create_book'),
    path(
        'is_read/<int:book_id>',
        views.book_is_read_view,
        name='is_read_book'
    ),
    path(
        'update/<int:book_id>',
        views.book_update_view,
        name='update_book'
    ),
    path(
        'delete/<int:book_id>',
        views.book_delete_view,
        name='delete_book'
    ),
]