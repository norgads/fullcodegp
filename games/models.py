from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import CustomUser

class Game(models.Model):
    title = models.CharField(max_length=255, 
                             verbose_name="Название игры")
    image = models.ImageField(upload_to='game_images', 
                              default='default.jpg', 
                              verbose_name="Изображение игры")
    
    description = models.TextField(verbose_name="Краткое описание игры")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата выхода")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    developer = models.CharField(max_length=100, verbose_name="Разработчик")
    publisher = models.CharField(max_length=100, verbose_name="Издатель")
    platform = models.CharField(max_length=255, verbose_name="Плафторма")
    edition = models.CharField(max_length=100, verbose_name="Тип издания")
    os_req = models.CharField(max_length=200, default="0", verbose_name="Операционная система")
    cpu_req = models.CharField(max_length=200, default="0", verbose_name="Процессор")
    ram_req = models.CharField(max_length=100, default="0", verbose_name="Оперативная память")
    gpu_req = models.CharField(max_length=200, default="0", verbose_name="Видеокарта")
    disk_req = models.CharField(max_length=50, default="0", verbose_name="Место на жестком диске")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL-метка")
    video_url = models.FileField(blank=True, upload_to='videos/',  verbose_name="Ссылка на видео")


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'  


class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshots')
    game = models.ForeignKey( Game,
        on_delete=models.CASCADE,
        related_name='screenshots'
    )

    def __str__(self):
        return f'Screenshot for {self.image}'

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'    


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.game}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'   