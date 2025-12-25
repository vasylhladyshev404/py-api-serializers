from rest_framework import serializers

from cimema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"    
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    cinema_hall = CinemaHallSerializer(
        many=False,
        read_only=True
    )
    movie = MovieSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"
