from django.db import models
from django.db.models import Sum
# Create your models here.


class Award(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField()

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name


class Artist(models.Model):
    """
    Table for Artist
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=72)
    dob = models.DateField()
    award = models.ManyToManyField(Award)
    gender =  models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name



class Movie(models.Model):
    """
    Table for Movies to be entered
    MTM relation to Artist and awards
    """
    name = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    release_date = models.DateField(max_length=80)
    avg_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    language = models.CharField(max_length=20)
    artist = models.ManyToManyField(Artist)
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    award = models.ManyToManyField(Award)


    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name

    def save(self, *args, **kwargs):
        all_ratings = Rating.objects.filter(movie__id = self.id)
        # breakpoint()
        total_rating = 0
        total_votes = all_ratings.aggregate(Sum('votes'))['votes__sum']
        if total_votes != None:
            for rating in all_ratings:
                total_rating += rating.rate * rating.votes
        else:
            total_rating = 0
            total_votes = 1
        self.avg_rating = total_rating / total_votes
        super(Movie, self).save(*args, **kwargs)


class Rating(models.Model):
    """
    Model to save movie and Its ratings
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
 

    def __str__(self):

        """
        String representation for the class on DB
        """
        return self.movie.name+str(self.rate)


