from django.db import models

# Create your models here.
#Table to store authors
class Author(models.Model):
    name = models.CharField(max_length=255)
    total_rating = models.FloatField(default=0.0)
    num_books = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    #updating total_rating
    def update_total_rating(self):
        reviews = Review.objects.filter(author=self)
        total_rating = sum(review.rating for review in reviews)
        num_reviews = len(reviews)

        if num_reviews > 0:
            self.total_rating = total_rating/num_reviews
        else:
            self.total_rating = 0
        self.save()

#Table to store books
class Book(models.Model):
    title = models.CharField(max_length=255)
    total_rating = models.FloatField(default=0.0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #updating total rating
    def update_total_rating(self):
        reviews = Review.objects.filter(book=self)
        total_rating = sum(review.rating for review in reviews)
        num_reviews = len(reviews)

        if num_reviews > 0:
            self.total_rating = total_rating/num_reviews
        else:
            self.total_rating = 0
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.author.num_books = self.author.book_set.count()
        self.author.save()

#single table to store reviews
class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField()
    total_rating = models.FloatField(default=0.0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)

