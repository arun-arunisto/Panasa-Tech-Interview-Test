from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ..models import Author, Book, Review


class TestUrls(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.client.login(username='testuser', password='testpassword')
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author)
        self.review = Review.objects.create(rating=4.0, comment="Test comment", author=self.author, book=self.book)

    def test_author_list_create_view_url(self):
        url = reverse('authors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Author list create url test failed")

    def test_book_list_create_view_url(self):
        url = reverse("books")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Book list create view url test failed")

    def test_book_update_view_url(self):
        url = reverse("books-update", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Book update url test failed")

    def test_review_create_view_url(self):
        url = reverse("reviews")
        data = {"rating": 4.0, "comment": "Test Comment", "author": self.author.id, "book": self.book.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Review list create view test failed")

    def test_author_review_list_view_url(self):
        url = reverse("author-review-list", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Author review listing test failed")
