from django.urls import path
from .views import (AuthorListCreateView, BookListCreateView,
                    BookUpdateView, ReviewCreateView, AuthorReviewListView)
urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name="authors"),
    path('books/', BookListCreateView.as_view(), name="books"),
    path('book/<int:pk>/', BookUpdateView.as_view(), name="books-update"),
    path('reviews/', ReviewCreateView.as_view(), name="reviews"),
    path('author/<int:author_id>/reviews/', AuthorReviewListView.as_view(), name="author-review-list")
]