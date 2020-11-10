from django.db import models


class Movie(models.Model):
	tmdb_id = models.IntegerField()
	imdb_id = models.CharField(max_length=256)
	vote_average = models.FloatField()
	vote_count = models.IntegerField()
	popularity = models.FloatField()


class Comment(models.Model):
	#link to user
	content = models.CharField(max_length = 144)
	created = models.DateField(auto_now = True)
	movie = models.ForeignKey(Movie, on_delete = models.CASCADE)