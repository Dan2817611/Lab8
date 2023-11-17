from django.shortcuts import render
from .models import Book, Reader, BookIssue


def index_page(request):
    books = Book.objects.all()
    readers = Reader.objects.all()
    book_issues = BookIssue.objects.all()

    return render(request, 'index.html', {'books': books, 'readers': readers, 'book_issues': book_issues})
