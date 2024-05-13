from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Player, Woodcutting


@receiver(post_save, sender=Player)
def create_skills_for_player(sender, instance, created, **kwargs):
    if created:
        Woodcutting.objects.get_or_create(player=instance)