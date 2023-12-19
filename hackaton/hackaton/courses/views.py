from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='')
def courses(requset):
    return render(requset, 'courses/courses.html')


@login_required(login_url='')
def password_courses(requset):
    return render(requset, 'courses/password.html')