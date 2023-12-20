from django.urls import path
from . import views

# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.courses, name="main_courses"),
    path('password_courses/', views.password_courses, name="password_courses"),
    path('scammers/', views.mosheniki, name="mosheniki_main"),
    path('scammers/viruses', views.mosheniki_viruses, name="mosheniki_viruses"),
    path('scammers/phishing', views.mosheniki_fishing, name="mosheniki_fishing"),
    path('scammers/financial_pyramid', views.mosheniki_fin_piromida, name="mosheniki_fin_piromida"),
    path('scammers/coshial_ingeering', views.mosheniki_coshial_ingeering, name="mosheniki_coshial_ingeering"),
]   