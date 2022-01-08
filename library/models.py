from django.db import models

# Create your models here.

class Book(models.Model):

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    is_read = models.BooleanField(default=False)
