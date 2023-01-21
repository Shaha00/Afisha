from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()


class MovieDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class ReviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()


class ReviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()
