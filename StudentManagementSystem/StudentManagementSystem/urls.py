"""
URL configuration for StudentManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Student.views import view_hello
from Student import views
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello1/', view_hello),
    path('',views.signupPage,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('homepage/',views.Homepage,name='home'),
    path('student/',views.student,name='studentinfo'),
    path('admission/',views.admission,name='admissioninfo'),
    path('marks/',views.marks,name='marksinfo'),
    path('feedback/',views.feedback,name='feedback'),
]
