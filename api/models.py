from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

def upload_path(instance, filename):
    return '/'.join(['covers',str(instance.title),filename])

# Create your models here.

class Booknumber(models.Model):
    isbn10 = models.CharField(validators=[MinLengthValidator(10)], max_length=10, unique=True)
    isbn13 = models.CharField(validators=[MinLengthValidator(13)], max_length=13, unique=True)


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=20)
    book = models.ManyToManyField('Book', related_name='authors')


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False)
    cover = models.ImageField(blank=True, null = True, upload_to=upload_path)

class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, null=False)
    bookNumber = models.OneToOneField(Booknumber, on_delete=models.CASCADE, null=False, blank=False)
    cover = models.ImageField(blank=True, null = True, upload_to=upload_path)

    def no_ratings(self):
        ratings = Rating.objects.filter(book=self)
        return len(ratings)

    def avg_ratings(self):
        ratings= Rating.objects.filter(book=self)
        sum = 0
        for i in ratings:
            sum=sum+i.rating

        if len(ratings)<1:
            return 0
        else:
            return sum/len(ratings)


class Character(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='books')

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')

    class Meta:
        unique_together=(('user','book'))
        index_together = (('user','book'))


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    age = models.PositiveSmallIntegerField()
    bio = models.CharField(max_length=256)

