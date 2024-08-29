from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):  # смотри 5,2
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # поле даты публикации
    created = models.DateTimeField(auto_now_add=True)  # поле даты создания
    updated = models.DateTimeField(auto_now=True)  # поле даты изменения
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]  # Индекс повысит производительность запросов

    def __str__(self):
        return self.title
