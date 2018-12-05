# books/tests.py

from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book, Chapter
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token


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


class ChapterApiTests(APITestCase):
    url = reverse("books:chapters")

    def setUp(self):
        self.username = "marcio.souza"
        self.email = "marcio.souza@ziggy.com"
        self.password = "stardust"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    @staticmethod
    def create_book(title, description, category, author):
        """
        Create a book to be used in chapter validation
        """
        return Book.objects.create(title=title, description=description, category=category, author=author)

    def test_create_chapter(self):
        """
        ensure we can create a book chapter
        """
        self.create_book("Morrissey","Smiths", "80s", "Me")
        response = self.client.post(self.url, {"title": "Apice", "content": "All world", "book": 1 })
        self.assertEqual(201, response.status_code)

    def test_chapter_list(self):
        """
        ensure we can create a book
        """
        client = APIClient()
        response = client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
