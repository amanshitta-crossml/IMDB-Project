from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path('date_sort/', views.date_sort, name="date_sort"),
	path('add_movie/',views.add_movies, name="add_movie"),
	path('add_artist/',views.add_artists, name="add_artist"),
	path('rate/',views.rate_movies, name="rate_movie"),
	# path('award/',views.give_award, name="give_award"),


]