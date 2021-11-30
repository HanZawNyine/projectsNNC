from os import name
from django.conf.urls import url
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
from . decorator import authenticated_user, admin_only, allowed_roles
from django.contrib.auth.models import Group


def home(request):
    lastAction = models.Movie.objects.filter(tags=3)
    lastDrama = models.Movie.objects.filter(tags=2)
    lastComedy = models.Movie.objects.filter(tags=1)

    return render(request, 'accounts/home.html', {
        "lastDrama": lastDrama.last(),
        "lastAction": lastAction.last(),
        "lastCodemy": lastComedy.last()
    })


@login_required(login_url='login')
def movie(request):
    mov = models.Movie.objects.filter(type='movie').order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
def all(request):
    mov = models.Movie.objects.all().order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
def series(request):
    mov = models.Movie.objects.filter(type='series').order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
def onemovies(request, id):
    onemov = models.Movie.objects.get(id=id)
    server = onemov.serverlink_set.all()
    return render(request, 'accounts/onemovie.html', {
        "onemovie": onemov,
        "servers": server
    })


@login_required(login_url='login')
@admin_only
@allowed_roles(roles=['admin'])
def dashboard(request):
    movie = models.Movie.objects.all().order_by('-created_at')
    countMovie = movie.count()
    user = models.Customer.objects.all()
    usertotal = user.count()
    return render(request, 'accounts/dashboard.html', {
        'movies': movie,
        'countmovie': countMovie,
        'usertotal': usertotal
    })


@login_required(login_url='login')
def action(request):
    mov = models.Movie.objects.filter(tags=3).order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
def drama(request):
    mov = models.Movie.objects.filter(tags=2).order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
def comedy(request):
    mov = models.Movie.objects.filter(tags=1).order_by('-created_at')
    return render(request, 'accounts/movie.html', {
        'mov': mov
    })


@login_required(login_url='login')
@admin_only
@allowed_roles(roles=['admin'])
def remove(request, id):
    movie = models.Movie.objects.get(id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('dashboard')
    return render(request, 'accounts/remove.html', {
        'movie': movie
    })


@login_required(login_url='login')
def search(request):
    if request.method == "POST":
        searchQuery = request.POST['searchinput']
        # print(searchQuery)
        mov = models.Movie.objects.filter(
            name__contains=searchQuery).order_by('-created_at')
        # print(mov)
        return render(request, 'accounts/movie.html', {
            'mov': mov
        })


@authenticated_user
def register(request):
    register = forms.RegisterForm()
    if request.method == "POST":
        register = forms.RegisterForm(request.POST)
        if register.is_valid:
            user = register.save()
            login(request, user)
            return redirect("customer_profile")
    return render(request, 'accounts/register.html', {
        'registerForm': register
    })


@authenticated_user
def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user,)
            return redirect('/')
        else:
            messages.error(request, "Username and Password invalid")
            return redirect('login')
    return render(request, "accounts/userlogin.html")


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def customerprofile(request):
    return render(request, 'accounts/customer_profiles.html')


@login_required(login_url='login')
def customerProfileSettings(request):
    form = forms.CustomerProfile(instance=request.user.customer)
    if request.method == "POST":
        form = forms.CustomerProfile(
            request.POST, request.FILES, instance=request.user.customer)
        if form.is_valid:
            form.save()
            return redirect('customer_profile')
    return render(request, 'accounts/customer_profiles_settings.html', {
        'forms': form
    })


@login_required(login_url='login')
@admin_only
@allowed_roles(roles=['admin'])
def updateMovie(request, id):
    mm = models.Movie.objects.get(id=id)
    movie = forms.OneMovieForm(instance=mm)

    if request.method == "POST":
        movie = forms.OneMovieForm(request.POST, instance=mm)
        if movie.is_valid:
            movie.save()
            return redirect(f'/movies.show/{id}')

    return render(request,  'accounts/updatemovie.html', {
        'updatemovie': movie,
        'imgUrl': mm.imageurl
    })
