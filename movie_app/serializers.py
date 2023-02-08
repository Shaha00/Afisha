from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ReviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieSerialize(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id movie_reviews rating title'.split()


class MovieDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.TextField()
    duration = serializers.TextField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):  # 100
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f"Director with ({director_id}) does not exists")
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.TextField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError(f"Movie with ({movie_id}) does not exists")
