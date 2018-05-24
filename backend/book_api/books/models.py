# books/models.py

from django.db import models


class Book (models.Model):
    """
    Book Model: a book is a collection of chapters created by one author
    A book has one or more categories, one front cover (a image size A4)
    A entire book can be downloaded by one user
    The book front-cover image should be by itself in the first page
    The book title and author name should be by itself in the second page
    """

    title = models.CharField(max_length=255)
    front_cover = models.ImageField(upload_to='covers/', default='covers/None/No-img.jpg')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=140)
    author = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title + ' (by: ' + self.author + ')'


class Chapter (models.Model):
    """
    A Chapter is which compose the book. Inside the chapters are the
    texts created by Book's Author. The book is ordered by chapters
    Chapter must start in the third page showing the “Chapter Title”
    at the beginning, then the  content, and at the end its creation date.
    A chapter can not start immediately after the end of the text of the prior chapter, but at the start of
    a new blank page. Each page should have a page number
    """

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'title')
        ordering = ['title']

    def __str__(self):
        return self.title + ' (from: ' + self.book.title + ')'
