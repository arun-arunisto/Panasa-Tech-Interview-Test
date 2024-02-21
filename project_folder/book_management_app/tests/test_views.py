from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Author, Book, Review


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.client.login(username='testuser', password='testpassword')
        self.author = Author.objects.create(
            name="Test Author"
        )
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author
        )
        self.review_data = Review.objects.create(
            rating=4.0,
            comment="Test Comment",
            author=self.author,
            book=self.book
        )

    def test_author_list_create_view(self):
        url = '/authors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Authors list view test failed")

        response = self.client.post(url, data={'name':'new test author'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Author create test failed")
        self.assertEqual(Author.objects.count(), 2, "Authors total count failed")

    def test_book_list_create_view(self):
        url = '/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Books list view test failed")

        response = self.client.post(url, data={"title":"New test book","author":self.author.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Book creation test failed")
        self.assertEqual(Book.objects.count(), 2, "Book count test failed")

    def test_book_update_view(self):
        url = f"/book/{self.book.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Selecting book for update failed")

        response = self.client.put(url, data={"title":"Updated test book", "author":self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Book update test failed")
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated test book", "Book updating test failed")

    def test_review_create_view(self):
        url = '/reviews/'
        response = self.client.post(url, data={'rating':4.0, 'comment':'Test comment', 'author':self.author.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Review for author test failed")

        response = self.client.post(url, data={'rating':3.5, 'comment':'Another comment', 'book':self.book.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Review for book test failed")

        response = self.client.post(url, data={'rating':2.5, 'comment':'Another comment', 'author':self.author.id, 'book':self.book.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Review for both author and book test failed")

    def test_author_review_list_view(self):
        url = f"/author/{self.author.id}/reviews/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Author review list test failed")
