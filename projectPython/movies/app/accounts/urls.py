from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('dashboard', views.Dashboard, name='dashboard'),
    path("movie", views.Home, name="movie"),
    path('movies/<str:id>', views.Movie, name='movies.show'),
    path('all_user', views.all_user, name='all_user'),
    path('add_movies', views.AddMovies, name='add.movies'),
    path('', views.Home, name='root'),
]
