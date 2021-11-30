from django.conf.urls import url
from django.shortcuts import redirect, render
from . import models
from accounts.forms import *


def Home(request):
    allMovie = models.Movie.objects.all()
    print(allMovie)
    return render(request, 'accounts/home.html', {
        'allMovie': allMovie
    })


def Dashboard(request):
    user = models.User.objects.all()
    movie = models.Movie.objects.all()
    movtotal = movie.count()
    print(movtotal)
    totaluser = user.count()
    return render(request, 'accounts/dashboard.html', {
        'users': user,
        'movietotal': movtotal,
        'totalUser': totaluser,
    })


def Movie(request, id):
    movie = models.Movie.objects.get(id=id)
    serverlink = movie.serverlink_set.all()
    print(serverlink)
    # return HttpResponse(id)
    return render(request, 'accounts/movie.html', {
        'movie': movie,
        'serverlinks': serverlink,
    })


def all_user(request):
    user = models.User.objects.all()
    return render(request, 'accounts/alluser.html', {
        'users': user
    })


def AddMovies(request):
    add = MovieForm()
    if request.method == "POST":
        add = MovieForm(request.POST)
        if add.is_valid():
            add.save()
        return redirect("root")

    return render(request, 'accounts/add_movies.html', {
        'addmovies': add
    })
