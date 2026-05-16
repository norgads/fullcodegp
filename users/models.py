from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, verbose_name="Аватар")
    bio = models.TextField(blank=True, verbose_name="О себе")
    comment_count = models.IntegerField(default=0, verbose_name="Кол-во комментариев")
    last_visit = models.DateTimeField(auto_now=True, verbose_name="Последний визит")

    is_staff = models.BooleanField(default=False, verbose_name="Доступ к админ-панели")
    is_superuser = models.BooleanField(default=False, verbose_name="Полный доступ")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'   