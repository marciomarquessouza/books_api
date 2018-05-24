# books/serializers.py

from rest_framework import serializers
from .models import Book, Chapter


class BookSerializer (serializers.ModelSerializer):
    chapters = serializers.StringRelatedField(many=True)
    front_cover = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'front_cover',
            'description',
            'category',
            'author',
            'date_created',
            'chapters',
        )


class ChapterSerializer (serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = (
            'title',
            'content',
            'created',
            'book',
        )
