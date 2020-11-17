from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Watchlist(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name = 'watchlists',null=True ,on_delete = models.SET_NULL)
    description = models.TextField(max_length=200)
    created_at = models.DateField(auto_now = True)
    movies = models.ManyToManyField("movies.Movie")

    def __str__(self):
        return self.name
