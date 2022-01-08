from django.contrib import admin

from library.models import Book 

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    '''
        Admin View for Book
    '''
    list_display = ('name', 'author', 'is_read',)
    list_filter = ('author', 'is_read',)
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)