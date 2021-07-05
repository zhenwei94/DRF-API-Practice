from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.decorators import action

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Movie.objects.create(title=title,cover=cover)
        return HttpResponse({'message': 'Movie created'}, status=200)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = BookListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print('create book')
        serializer = BookCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def post(self, request, *args, **kargs):
        print('post book')
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)

    @action(detail = True, methods = ['POST'])
    def rate_book(self,request, pk=id):
        if ('rating' in request.data):
            book = Book.objects.get(id=pk)
            user = request.user
            ratings = request.data['rating']
            print(book.title)
            print(user.id)
            print(ratings)
            try:
                #If rating exist for the unique index (user,movie)
                print('Updating rating')
                rating = Rating.objects.get(user=user.id, book=book.id)
                rating.rating = ratings
                rating.save()
            except:
                #If rating does not exist (NEW)
                print('Creating new rating')
                rating = Rating.objects.create(user=user, book=book, rating=ratings)
            serializer = RatingSerializer(rating, many=False)
            response = {'message': f'it\'s working {pk}', 'result':serializer.data}
            return Response(response, status = status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class BooknumberViewSet(viewsets.ModelViewSet):
    queryset = Booknumber.objects.all()
    serializer_class = BooknumberSerializer
    authentication_classes = (TokenAuthentication,)


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = (TokenAuthentication,)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)

