from django.shortcuts import render


# Создаём функции для вывода html страницы


def regestration(requset):
    return render(requset, 'regestration/regestration.html')


def enterens(requset):
    return render(requset, 'regestration/enterens.html')


def profile_view(requset):
    return render(requset, 'regestration/profile.html')