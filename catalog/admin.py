from django.contrib import admin

from .models import *


admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', 'slug',('date_of_birth', 'date_of_death'))
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'slug')
        }),

        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )