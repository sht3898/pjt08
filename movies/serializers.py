from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreDetailSerializers(serializers.ModelSerializer):
    movie_set = MovieSerializers(many=True)
    class Meta(GenreSerializers.Meta):
        fields = GenreSerializers.Meta.fields + ['movie_set']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['content', 'score']