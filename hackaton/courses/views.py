from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Главная
@login_required(login_url='')
def courses(requset):
    return render(requset, 'courses/courses.html')


# Курс про пароль
@login_required(login_url='')
def password_courses(requset):
    return render(requset, 'courses/password.html')




#-----------------МОШЕННИКИ--------------------#

# Главная курсов про мошеннечество
@login_required(login_url='')
def mosheniki(requset):
    return render(requset, 'courses/mosheniki/main.html')


# Мошенники > вирусы
@login_required(login_url='')
def mosheniki_viruses(requset):
    return render(requset, 'courses/mosheniki/viruses.html')


# Мошенники > фишинг
@login_required(login_url='')
def mosheniki_fishing(requset):
    return render(requset, 'courses/mosheniki/phishing.html')


# Мошенники > финансовая пирамида
@login_required(login_url='')
def mosheniki_fin_piromida(requset):
    return render(requset, 'courses/mosheniki/fin_piromida.html')


# Мошенники > социальная инжинерия 
@login_required(login_url='')
def mosheniki_coshial_ingeering(requset):
    return render(requset, 'courses/mosheniki/coshial_ingeering.html')

#-----------------МОШЕННИКИ-КОНЕЦ--------------------#