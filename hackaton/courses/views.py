from django.shortcuts import render


def courses(requset):
    return render(requset, 'courses/courses.html')