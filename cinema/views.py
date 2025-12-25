from rest_framework import viewsets
from cimema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("cinema_hall", "movie")
        return queryset

    def get_serializer(self):
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionSerializer
