# books/urls.py

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'books'

urlpatterns = {
    # Frontend: index page
    url(r'^$',
        views.index,
        name="index"),

    # List all books
    url(r'^book/$',
        views.BookList.as_view(),
        name="books"),

    # Book detail
    url(r'^book/(?P<pk>[0-9]+)/$',
        views.BookDetail.as_view(),
        name="book_detail"),

    # List all chapters
    url(r'^chapter/$',
        views.ChapterList.as_view(),
        name="chapters"),

    # Chapter detail
    url(r'^chapter/(?P<pk>[0-9]+)/$',
        views.ChapterDetail.as_view(),
        name="chapter_detail"),

    # Chapter by book id
    url(r'^book/(?P<book_id>[0-9]+)/chapter/$',
        views.ChapterByBook.as_view(),
        name="chapter_by_book"),

    # Chapter detail by book id
    url(r'^book/(?P<book_id>[0-9]+)/chapter/(?P<pk>[0-9]+)/$',
        views.ChapterDetailByBook.as_view(),
        name="chapter_detail_by_book"),

    # PDF creation by book id
    url(r'^book/(?P<book_id>[0-9]+)/pdf/$',
        views.BookPdf.as_view(),
        name='book_pdf'),

    # PDF creation by chapter id
    url(r'^chapter/(?P<chapter_id>[0-9]+)/pdf/$',
        views.ChapterPdf.as_view(),
        name='chapter_pdf'),

    # PDF creation by book id and listing the chapters (only to follow the URLs logic)
    url(r'^book/(?P<book_id>[0-9]+)/chapter/pdf/$',
        views.BookPdf.as_view(),
        name='book_pdf'),

    # PDF creation by book and chapter id
    url(r'^book/(?P<book_id>[0-9]+)/chapter/(?P<chapter_id>[0-9]+)/pdf/$',
        views.BookChapterPdf.as_view(),
        name='book_chapter_pdf'),
}

urlpatterns = format_suffix_patterns(urlpatterns)