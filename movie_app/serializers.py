from django.template.defaultfilters import title
from rest_framework import serializers
from .models import Director,Movie,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'stars', 'text', 'movie']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'reviews', 'ratings']

    def get_ratings(self, obj):
        reviews = Review.objects.filter(movie=obj)
        if reviews.exists():
            return sum([review.stars for review in reviews])/len(reviews)
        return 0

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ['id','name','movies_count']


