from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sales.models import Student

user1=None
# Create your views here.
def login_fun(request):
    global user1
    global user
    if request.method=='POST':
        name=request.POST['txtname']
        password=request.POST['txtpassword']
        user=authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                user1="admin"
                return render(request,'home.html')
            elif user.is_authenticated:
                return render(request,'home.html',{"sales":True,"user":user})
            else:
                pass
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')


def signup_fun(request):
    if request.method=='POST':
        name=request.POST['txtname1']
        email=request.POST['txtemail']
        password=request.POST['txtpassword1']

        if User.objects.filter(Q(username=name)| Q(email=email)).exists():
            data= {'msg':True}
            return render(request, 'signup.html',data)
        else:
            user1=User.objects.create_user(username=name,email=email,password=password)
            user1.save()
            return redirect('log')
    else:
        return render(request,'signup.html')


def addstudent(request):
    if request.method== "POST":
        s1=Student()
        if user1 =="admin":
            s1.sales_person_id= request.POST["sales_person"]
        else:
            s1.sales_person=user


        s1.joiningdate=request.POST["txtdate"]
        s1.name=request.POST["txtname"]
        s1.age=request.POST["txtage"]
        s1.mobile=request.POST["txtmobile"]
        s1.email=request.POST["txtemail"]
        s1.education=request.POST["txteducation"]
        s1.skills=request.POST["txtskills"]
        s1.save()
        return render(request,'display.html')

    else:
        if user1=="admin":
            users=User.objects.all()
            return render(request,'add.html',{"users":users,"salesperson":True})
            # return render(request,'add.html')
        else:
            return render(request,'add.html',{"salesperson": False})


def displaymystudent(request):
    if user1 == "admin":
        students=Student.objects.all()
        return render(request,'display.html',{"students": students,"salesperson":True,"update":True})
    else:
        students=Student.objects.filter(sales_person=user)
        return render(request, 'display.html', {"students": students,"salesperson":False,"update":False})



def home(request):
    if user1=="admin":
        return render(request,'home.html')
    else:
        return render(request, 'home.html',{"sales":True,"user":user})



def update_student(request,id):
    users=User.objects.all()
    s1=Student.objects.get(id=id)

    if request.method == "POST":
        s1.sales_person_id = request.POST["sales_person"]
        s1.joiningdate = request.POST["txtdate"]
        s1.name = request.POST["txtname"]
        s1.age = request.POST["txtage"]
        s1.mobile = request.POST["txtmobile"]
        s1.email = request.POST["txtemail"]
        s1.education = request.POST["txteducation"]
        s1.skills = request.POST["txtskills"]
        s1.save()
        return redirect('display')
    else:
        return render(request,'add.html',{"users":users,"student":s1,"salesperson":True})


def delete_student(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect("display")