from django.shortcuts import render
from .models import Book, Borrower

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'library/borrower_list.html', {'borrowers': borrowers})
def dashboard(request):
    total_books = Book.objects.count()
    total_borrowers = Borrower.objects.count()
    return render(request, 'library/dashboard.html', {
        'total_books': total_books,
        'total_borrowers': total_borrowers,
    })