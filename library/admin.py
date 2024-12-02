from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    readonly_fields = ('id', 'due_back', 'status')
    can_delete = False
    extra = 0  # išjungia papildomas tuščias eilutes įvedimui


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    list_editable = ('due_back', 'status')
    search_fields = ('id', 'book__title')

    fieldsets = (
        ('General', {'fields': ('id', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
