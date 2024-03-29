from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Genre(models.Model):
    """model representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """string for representing the model object"""
        return self.name


from django.urls import reverse

class Book(models.Model):
    """model representing a generic book"""
    title = models.CharField(max_length=200)

    # foreign key used bc book can only have one author, but authors can have multiple books
    # author as a string rather than object bc it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # manytomanyfield bc genre can contain many books. books can cover many genres
    # genre class has already been defined so we can specify the object above
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    # foreign key because apparently books can only have one language, but a language can be used in many books
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        """string for representing the model object"""
        return self.title

    def get_absolute_url(self):
        """returns the url to accesss a detail record for this book"""
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """create a string for the genre. this is requried to display genre in admin"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

import uuid
import datetime

class BookInstance(models.Model):
    """model representing a specific copy of a book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across the whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
     )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """string for representing the model object"""
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    """model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """returns the url to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """string for representing the model object"""
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    """model representing a language (english, french, etc)"""
    name = models.CharField(max_length=200, help_text="Enter the books natural language")

    def __str__(self):
        """string for representing the moddel object"""
        return self.name


