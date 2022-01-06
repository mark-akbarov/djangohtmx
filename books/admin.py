from books.models import Author, Book
from django.contrib import admin


class BookLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookLineAdmin]


admin.site.register(Author, AuthorAdmin)