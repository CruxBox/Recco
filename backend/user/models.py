from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ## add multiple fields later
    contribution = models.IntegerField(blank=True,null=True,default=0)



    def __str__(self):
        return self.username

    def get_owned_watchlists(self):
        return self.watchlists.all()

    def get_shared_watchlists(self):
        return self.shared_watchlists.all()
    
    def get_favourite_watchlist(self):
        return self.watchlists.filter(name="Favourites").first()
    
    def get_seen_watchlist(self):
        return self.watchlists.filter(name="Seen").first()

    @property
    def get_favourite_watchlist_id(self):
        return self.watchlists.filter(name="Favourites").first().id
    
    @property
    def get_seen_watchlist_id(self):
        return self.watchlists.filter(name="Seen").first().id
