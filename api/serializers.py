from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import transaction


class BooknumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booknumber
        # exclude = ['id']
        exclude = []

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['id']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ['id']


class PersonSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Person
        fields = ['age','bio']


class UserSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=False)
    class Meta:
        model = User
        fields=['id','username','password','person']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    @transaction.atomic
    def create(self, validated_data):
        person_data = validated_data.pop('person')
        user = User.objects.create_user(**validated_data)
        user.person = Person.objects.create(user=user, **person_data)
        user.save()
        Token.objects.create(user=user)
        return user

class RatingSerializer(serializers.ModelSerializer):
    # book = BookSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Rating
        exclude = ['id']

class BookListSerializer(serializers.ModelSerializer):
    ratings=RatingSerializer(many=True)
    bookNumber = BooknumberSerializer(many=False)
    authors = AuthorSerializer(many=True)


    class Meta:
        model = Book
        fields=['title', 'description','ratings','bookNumber','authors']
        # exclude = ['id']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'cover']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    bookNumber = BooknumberSerializer(many=False)
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Book
        fields=['title', 'cover', 'description','authors','bookNumber','no_ratings', 'avg_ratings', 'ratings']
        # exclude = ['id']


class BookCreateSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True, read_only=True)
    # bookNumber = BooknumberSerializer(many=False)
    # ratings = RatingSerializer(many=True)

    class Meta:
        model = Book
        fields=['title', 'cover', 'description','authors','bookNumber','no_ratings', 'avg_ratings']
        # exclude = ['id']