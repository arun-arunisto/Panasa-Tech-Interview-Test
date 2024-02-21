from django.test import TestCase
from ..models import Author, Book, Review

class TestModels(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', author=self.author)
        self.review = Review.objects.create(
            rating=4.0,
            comment='Test Comment',
            author=self.author,
            book=self.book
        )

    def test_author_update_total_rating(self):
        self.author.update_total_rating()
        self.assertEqual(self.author.total_rating, 4.0, "Author total rating model test failed")

    def test_book_update_total_rating(self):
        self.book.update_total_rating()
        self.assertEqual(self.book.total_rating, 4.0, "Book total rating model test failed")

    def test_book_save_updates_author_num_books(self):
        initial_num_books = self.author.num_books
        new_book = Book.objects.create(title="New test book", author=self.author)
        self.assertEqual(self.author.num_books, initial_num_books+1, "Author num books model test failed")



