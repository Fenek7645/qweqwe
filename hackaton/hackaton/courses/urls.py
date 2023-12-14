from django.urls import path
from . import views

# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.courses, name="main_courses"),

]