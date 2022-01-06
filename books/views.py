from django.shortcuts import redirect, render

from .models import Author, Book
from .forms import BookForm, BookFormSet


def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
             book = form.save(commit=False)
             book.author = author
             book.save()
             return redirect("detail-book", pk=book.id)

        else:
            return render(request, "partials/book_form.html")

    context = {
        "form": form,
        "author": author
    }

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "partials/book_form.html", context)


def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }

    return render(request, "partials/book_detail.html", context)