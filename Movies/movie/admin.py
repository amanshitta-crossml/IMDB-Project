from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Award)
admin.site.register(Artist)