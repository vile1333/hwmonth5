from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status

@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    #step 1: Collect all directors from DB(QuerySet)
    directors = Director.objects.all()

    #step 2: Reformat QuerySet to List of dictionary
    list_ = DirectorSerializer(instance=directors, many=True).data

    #step 3: Return response as data and status(200)
    return Response(data=list_)

@api_view(http_method_names=['GET'])
def director_detail_api_view(request,id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    list_ = MovieSerializer(instance=movies, many=True).data
    return Response(data=list_)

@api_view(http_method_names=['GET'])
def movie_detail_api_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=list_)

@api_view(http_method_names=['GET'])
def review_detail_api_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def movie_review_list_api_view(request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
