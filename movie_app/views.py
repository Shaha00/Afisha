from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, DirectorDetailSerializer, MovieDetailSerialize, MovieSerialize, ReviewSerialize, ReviewDetailSerialize
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET', 'POST', 'PUT'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(name=name)
        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        name = request.data.get('name')

        director.name = name

        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerialize(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieDetailSerialize(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieDetailSerialize(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        return Response(data=DirectorDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT'])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerialize(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewDetailSerialize(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewDetailSerialize(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review.text = text
        review.stars = stars
        review.movie_id = movie_id
        return Response(data=ReviewDetailSerialize(review).data,
                        status=status.HTTP_201_CREATED)
