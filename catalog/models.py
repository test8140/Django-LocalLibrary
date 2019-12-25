from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre)

    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])

    
    def __str__(self):
        return self.title

    

class BookInstance(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')


    class Meta:
        ordering = ['due_back']

    
    def __str__(self):
        return '{0}({1})' .format(self.slug, self.book.title)


class Author(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

   
    def get_absolute_url(self):
       return reverse('author-detail', args=[str(self.slug)])


    def __str__(self):
        return '{0}{1}' .format(self.last_name, self.first_name)

