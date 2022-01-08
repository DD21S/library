from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from library.models import Book

# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'library/list.html'
    context_object_name = 'books'

def book_create_view(request):
    if 'action' in request.POST:
        new_book = Book.objects.create(
            name=request.POST['name'],
            author=request.POST['author']
        )

        new_book.save()

    return HttpResponseRedirect(reverse('library:books'))

def book_is_read_view(request, book_id):
    db_book = get_object_or_404(Book, pk=book_id)

    if db_book.is_read:
        db_book.is_read = False
    else:
        db_book.is_read = True

    db_book.save()

    return HttpResponseRedirect(reverse('library:books'))

def book_update_view(request, book_id):
    db_book = get_object_or_404(Book, pk=book_id)

    if 'action' in request.POST:
        db_book.name = request.POST['name']
        db_book.author = request.POST['author']
        db_book.save()

        return HttpResponseRedirect(reverse('library:books'))

    return render(request, 'library/update.html', {'book': db_book})

def book_delete_view(request, book_id):
    db_book = get_object_or_404(Book, pk=book_id)
    db_book.delete()

    return HttpResponseRedirect(reverse('library:books'))



