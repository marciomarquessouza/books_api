# books/urls.py

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = {
    url(r'^book/$', views.BookList.as_view(), name="books"),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name="book_detail"),
    url(r'^chapter/$', views.ChapterList.as_view(), name="chapters"),
    url(r'^chapter/(?P<pk>[0-9]+)/$', views.ChapterDetail.as_view(), name="chapter_detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)