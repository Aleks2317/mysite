from django.urls import path
from .views import post_list, post_detail

#  определяется именное пространство приложения с помощью переменной app_name
app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),

]
