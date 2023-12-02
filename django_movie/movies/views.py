from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import (MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer, ActorSerializer, ActorDetailSerializer, CategorySerializer)
from django_filters.rest_framework import DjangoFilterBackend
from .service import MovieListFilter





class MovieListView(generics.ListAPIView):
    '''Вывод списка фильмов'''
    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieListFilter
    def get_queryset(self):
        return Movie.objects.filter(draft = False)




class MovieDetailView(generics.RetrieveAPIView):
    '''Вывод  фильма'''
    serializer_class = MovieDetailSerializer
    def get_queryset(self):
        return Movie.objects.filter(draft = False)



class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer

class Category_list(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class ActorList(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer



class AddStarRatingView(APIView):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
