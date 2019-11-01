from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from .models import Genre, Movie, Review
from .serializers import GenreSerializers, GenreDetailSerializers, MovieSerializers, ReviewSerializer

# Create your views here.
@api_view(['GET'])
def genre_index(request):
    '''
    장르 정보
    '''
    genres = Genre.objects.all()
    serializer = GenreSerializers(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    '''
    장르 상세 정보
    '''
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializers(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_index(request):
    '''
    영화 정보
    '''
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    영화 상세 정보
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)

@api_view(['POST'])
def reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    '''
    평점 등록
    '''
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id = movie_pk)
    return Response({'message':'작성되었습니다.'})
    

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})