from django.shortcuts import render, redirect
from .forms import MovieForm, ArtistForm, RatingForm
from .models import Movie, Rating, Artist
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
# Create your views here.


def index(request):
    """
    function to view index page
    """
    if request.method == "POST":
        if request.POST['sort_by'] == "Top 10":
            movies = Movie.objects.order_by('-avg_rating')[:10]
        elif request.POST['sort_by'] == "Last 10":
            movies = Movie.objects.order_by('avg_rating')[:10]
        
        context = {'movies':movies}
        # return render(request, 'movie/sort.html', context)
    elif request.GET:
        name = request.GET['search']
        movies = Movie.objects.filter(name__icontains=name)
        if movies:
            movies = Movie.objects.filter(name__icontains=name)
        else:
            artist = Artist.objects.filter(name__icontains=name)
            movies = artist[0].movie_set.all()

        context = {'movies':movies}

    else:   
        movies = Movie.objects.all()
        context = {'movies':movies}
    return render(request, 'movie/index.html', context)

    

def add_movies(request):
    """
    function to add movies
    """
    if request.method == "POST":
        # breakpoint()
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added !")
            return redirect(reverse('add_movie'))
        else:
            messages.error(request, "Error Occured")
            return redirect(reverse('add_movie'))
    else:

        movie_form = MovieForm()
        context = {'form':movie_form}
    return render(request, 'movie/add_movie.html', context)


def add_artists(request):
    """
    function to add a new artist to the tabel
    """
    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        # breakpoint()
        if artist_form.is_valid():
            artist_form.save()
            messages.success(request, "Successfully Added !")
            return redirect(reverse('add_artist'))
        else:
            messages.error(request, "Error Occured")
            return redirect(reverse('add_artist'))
    else:
        artist_form = ArtistForm()
        context = {'form':artist_form}
    
    return render(request, 'movie/add_artist.html',context)

# def get_avg_rating():
#     movies = Movies.objects.all()
#     for movie in movies:


def rate_movies(request):
    """
    function to rate Movies
    """
    
    if request.method == "POST":
        rate_form = RatingForm(request.POST)
        # print(type(rate_form))
        if rate_form.is_valid():
            form_object =  rate_form.save(commit=False)
            form_object.movie = rate_form.cleaned_data.get('movie')
            form_object.rate = rate_form.cleaned_data['rate']
            
            filtered_data = Rating.objects.filter(movie=form_object.movie, rate=form_object.rate)

            if filtered_data.count() >= 1:
                rate_obj = filtered_data.get()
                rate_obj.votes += 1
                rate_obj.save()
                rate_obj.movie.save()
            else:
                form_object.votes = 1
                form_object.save()
                form_object.movie.save()

            messages.success(request, "Rated Successfully !")
            # TODO -> Average rating Logic
            return redirect(reverse('rate_movie'))
        else:
            messages.error(request, "Error While Rating ")
            return redirect(reverse('rate_movie'))

    else:
        rate_form = RatingForm()
        context = {'form':rate_form}
        return render(request, 'movie/rate_movie.html', context)


def date_sort(request):
    """
    function to sort movies within a range of date
    """
    if request.POST:
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # breakpoint()
        movies = Movie.objects.filter(release_date__range=[from_date,to_date])
        context = {'movies':movies}
    else:
        movies = Movie.objects.none()
        context = {'movies':movies}
    return render(request, 'movie/date_sort.html', context)



def give_award(request):


    context = {}
    return render(request, 'movie/award.html', context)