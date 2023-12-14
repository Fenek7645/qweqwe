from django.urls import path
from . import views



# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('/', views.regestration, name="reg_home"),
    path('enterens/', views.enterens, name="enterens"),
    path('profile/', views.profile_view, name="profile"),
]