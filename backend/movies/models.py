from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User

class Movie(models.Model):
	tmdb_id = models.IntegerField()
	imdb_id = models.CharField(max_length=256, null = True)
	vote_average = models.FloatField(null = True)
	vote_count = models.IntegerField(null = True)
	popularity = models.FloatField(null = True)
	# genre = models.CharField(max_length=100, default = "Thriller")

	def __str__(self):
		return str(self.tmdb_id);

class Comment(models.Model):
	content = models.CharField(max_length = 144)
	created = models.DateField(auto_now = True)
	movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'comments')
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_comments')
	score = models.IntegerField(default = 0, null=False)

class Rating(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE) 
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	rating = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])

	def __str__(self):
		return self.user.username + " " + str(self.movie.tmdb_id) + " " + str(self.rating)