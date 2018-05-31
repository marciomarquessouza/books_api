# books/views.py

from rest_framework import generics
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from .render import Render
from django.shortcuts import render
from django.views.generic import View


class BookList(generics.ListCreateAPIView):
    """ DRF view to list all books """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """ DRF view with book details """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterList (generics.ListCreateAPIView):
    """ DRF view to show all chapters """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ChapterDetail (generics.RetrieveUpdateDestroyAPIView):
    """ DRF view with book details """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ChapterByBook (generics.ListCreateAPIView):
    """ DRF view to show all chapters from one specific book """
    serializer_class = ChapterSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Book.objects.get(pk=book_id).chapters.all()


class ChapterDetailByBook (generics.RetrieveUpdateDestroyAPIView):
    """ DRF view to show all chapters from one specific book """
    serializer_class = ChapterSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Book.objects.get(pk=book_id).chapters.all()


class BookPdf(View):
    """
    View respnsible to create PDF for a entire Book
    """

    def get(self, request, book_id):
        """ Receive the PDF request and call the PDF render to convert the HTML to PDF"""

        book = Book.objects.get(id=book_id)
        chapters = book.chapters.all()
        params = {
            'book': book,
            'chapters': chapters,
            'request': request
        }

        file_name = book.title

        return Render.render('book.html', params, file_name)


class ChapterPdf(View):
    """
    View respnsible to create a PDF for a Specific Chapter
    """

    def get(self, request, chapter_id):
        """ Receive the PDF request and call the PDF render to convert the HTML to PDF"""

        chapters = []
        chapter = Chapter.objects.get(pk=chapter_id)
        book = chapter.book
        chapters.append(chapter)
        params = {
            'book': book,
            'chapters': chapters,
            'request': request
        }

        file_name = book.title + ' (chapter_' + chapter.title + ')'

        return Render.render('book.html', params, file_name)


class BookChapterPdf(View):
    """
    View respnsible to create PDF for a specific chapter for a specific Book
    """

    def get(self, request, book_id, chapter_id):
        """ Receive the PDF request and call the PDF render to convert the HTML to PDF"""

        chapters = []

        book = Book.objects.get(id=book_id)
        chapter = book.chapters.get(pk=chapter_id)
        chapters.append(chapter)
        params = {
            'book': book,
            'chapters': chapters,
            'request': request
        }

        file_name = book.title + ' (chapter_' + chapter.title + ')'

        return Render.render('book.html', params, file_name)


def index(request):
    """ Frontend index """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'frontend/index.html', context)
