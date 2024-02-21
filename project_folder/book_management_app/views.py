from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = serializer.save()
        author.num_books = author.book_set.count()
        author.save()

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.author:
            instance.author.update_total_rating()
            instance.total_rating = instance.author.total_rating
        if instance.book:
            instance.book.update_total_rating()
            instance.total_rating = instance.book.total_rating
        instance.save()

class AuthorReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        author = Author.objects.get(pk=author_id)
        author.update_total_rating() #to make total_rating up-to-date
        reviews = Review.objects.filter(author=author)
        for review in reviews:
            review.total_rating = author.total_rating
            review.save()
        return reviews