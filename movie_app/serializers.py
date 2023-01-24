from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class ReviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ReviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieSerialize(serializers.ModelSerializer):
    movie_reviews = ReviewSerialize(many=True)

    class Meta:
        model = Movie
        fields = 'id movie_reviews rating title'.split()


class MovieDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()
