from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from watchlists.models import Watchlist

User=get_user_model()
@receiver(post_save,sender=User)
def create_default_wacthlists(sender, instance, created, **kwargs):
    if created:
        favourite = Watchlist.objects.create(owner=instance,name="Favourites",description="My favourites")
        seen = Watchlist.objects.create(owner=instance,name="Seen",description="My seen list")
        favourite.save()
        seen.save()
