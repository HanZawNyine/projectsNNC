from os import name
from django.urls import path, include

from accounts import models
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('movies', views.movie, name='movies'),
    path('all_movies', views.all, name='all'),
    path('series', views.series, name='series'),
    path('movies.show/<int:id>', views.onemovies, name="onemovies"),
    path('action', views.action, name='action'),
    path('comedy', views.comedy, name='comedy'),
    path('drama', views.drama, name='drama'),
    path('remove/<int:id>', views.remove, name="remove"),
    path('search', views.search, name='searchmovies'),
    path('register', views.register, name="register"),
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name='logout'),
    path("customerprofile", views.customerprofile, name="customer_profile"),
    path('customerprofile/settings', views.customerProfileSettings,
         name="profilesettings"),
    path('updatemovie/<int:id>', views.updateMovie, name="updatemovies")
]
