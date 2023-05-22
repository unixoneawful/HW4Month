from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_view(request):
    return HttpResponse("Hello This is my first project Django")


def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})