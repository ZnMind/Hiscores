from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=255, unique=True, null=False)
    
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        print(is_new)
        if is_new:
            Woodcutting.objects.create(player=self)


class Woodcutting(models.Model):
    player = models.OneToOneField(
        "skills.Player", 
        on_delete=models.CASCADE, 
        related_name='woodcutting'
    )
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    experience_last = models.IntegerField(default=0)
    experience_next = models.IntegerField(default=75)

    def save(self, *args, **kwargs):
        while self.experience >= self.experience_next:
            self.experience_last = self.experience_next
            next_exp = 100 * pow(2, self.level / 8)
            rounded = round(next_exp, 0)
            self.experience_next = self.experience_next + int(rounded)
        super().save(*args, **kwargs)
