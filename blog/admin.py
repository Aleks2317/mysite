from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # отображаемые поля
    list_filter = ['status', 'created', 'publish', 'author']  # позволяет фильтровать результаты по полям
    search_fields = ['title', 'body']  # строка поиска
    prepopulated_fields = {'slug': ('title', )}  # slug заполняется автоматически.
    raw_id_fields = ['author']  # оле author отображается поисковым виджетом
    autocomplete_fields = ['author']
    date_hierarchy = 'publish'  # навигационные ссылки для навигации по иерархии дат
    ordering = ['status', 'publish']  # по умолчанию посты упорядочены по столбцам

