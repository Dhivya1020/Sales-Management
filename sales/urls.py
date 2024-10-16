from django.urls import path

from sales import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('signup/',views.signup_fun,name='signup'),
    path('home/',views.home,name='home'),
    path('add/',views.addstudent,name='add'),
    path('display/',views.displaymystudent,name='display'),
    path('update/<int:id>',views.update_student,name='update'),
    path('delete/<int:id>',views.delete_student,name='delete'),
]