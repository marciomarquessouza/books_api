# books/tests.py

from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Chapter
from rest_framework.test import APIClient


class ChapterModelTest(TestCase):

    def test_content_in_paragraph_return(self):
        """
        content_in_paragraph() return paragraphs from the content.
        """
        content_test = 'Paragraph 1 \n Paragraph 2 \n Paragraph 3'
        chapter = Chapter(content=content_test)
        self.assertIs(len(chapter.content_in_paragraph()), 3)

        content_test = 'Paragraph 1'
        chapter = Chapter(content=content_test)
        self.assertIs(len(chapter.content_in_paragraph()), 1)

    def test_content_in_paragraph_type(self):
        """
        content_in_paragraph() type return is equal to list.
        """
        chapter = Chapter(content='Text')
        self.assertIs(type(chapter.content_in_paragraph()), list)

    def test_content_in_paragraph_when_empty(self):
        """
        content_in_paragraph() receive a empty value
        """
        chapter = Chapter(content='')
        self.assertIs(type(chapter.content_in_paragraph()), list)
        self.assertIs(len(chapter.content_in_paragraph()), 0)


class BookApiTests(APITestCase):

    def test_book_list(self):
        """
        ensure we can create a book
        """
        client = APIClient()
        response = client.get('/book/')
        self.assertEqual(response.status_code, 200)

    def test_chapter_list(self):
        """
        ensure we can create a book
        """
        client = APIClient()
        response = client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
