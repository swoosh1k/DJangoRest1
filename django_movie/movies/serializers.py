from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    '''Список Фильмов'''

    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')




class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'



# class DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ('id', 'name', 'age')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    '''Добавление отзыва'''
    class Meta:
        model = Review
        fields = '__all__'

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('star', 'movie')

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(ip = validated_data.get('ip', None),
                                                 movie = validated_data.get('movie', None),
                                                 defaults ={'star': validated_data.get('star')})
        return rating
class ReviewsSerializer(serializers.ModelSerializer):
    '''Вывод отзыва'''
    class Meta:
        model = Review
        fields = ('name', 'text', 'parent')


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field = 'name', read_only = True )
    directors = serializers.SlugRelatedField(slug_field = 'name', read_only=True, many = True)
    genre = serializers.SlugRelatedField(slug_field = 'name', read_only=True, many = True)
    actors = ActorSerializer(read_only=True, many = True )
    reviews = ReviewsSerializer( many = True)

    """Полный фильм"""
    class Meta:
        model = Movie
        exclude = ('draft',)





