from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    '''Метод get_queryset() менеджера возвращает набор запросов QuerySet, который будет исполнен.
    Мы переопределили этот метод, чтобы сформировать конкретно-прикладной набор запросов QuerySet,
    фильтрующий посты по их статусу и возвращающий поочередный набор запросов QuerySet,
    содержащий посты только со статусом PUBLISHED.'''
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


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

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]  # Индекс повысит производительность запросов

    def __str__(self):
        return self.title
