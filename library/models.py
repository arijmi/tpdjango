from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
