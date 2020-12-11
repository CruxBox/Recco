from django.db import models

from user.models import User

class Movie(models.Model):
	tmdb_id = models.IntegerField()
	imdb_id = models.CharField(max_length=256, null = True)
	vote_average = models.FloatField(null = True)
	vote_count = models.IntegerField(null = True)
	popularity = models.FloatField(null = True)

	def __str__(self):
		return str(self.tmdb_id);


class Comment(models.Model):
	content = models.CharField(max_length = 144)
	created = models.DateField(auto_now = True)
	movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'comments')
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_comments')
	score = models.IntegerField(default = 0, null=False)
