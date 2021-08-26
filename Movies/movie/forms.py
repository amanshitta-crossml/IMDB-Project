from django.forms import ModelForm
from .models import Movie, Artist, Rating
from django import forms

class MovieForm(ModelForm):
	# name = forms.CharField(max_length=72, required=True)
	
	class Meta:
		model = Movie
		fields = ['name','genre','release_date','language','artist','duration']


class ArtistForm(ModelForm):
	class Meta:
		model = Artist
		fields = "__all__"



class RatingForm(ModelForm):
	RATING_CHOICES = [(i,i) for i in range(1,11)]
	rate = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=RATING_CHOICES)
	# votes = form.
	class Meta:
		model = Rating
		fields = ['movie','rate']

	
	