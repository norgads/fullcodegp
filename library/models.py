from django.db import models
from games.models import Game
from users.models import CustomUser

class LibraryGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"

    class Meta:
        verbose_name = 'Игра в библиотеке'
        verbose_name_plural = 'Игры в библиотеке'