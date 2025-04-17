from django.shortcuts import render
from student.forms import Registration,Login
# Create your views here.
def registration(request):
    fm = Registration()
    return render(request,'student/registration.html',{'form':fm})

def login(request):
    lg = Login()
    # lg = Login(auto_id='anji_%S')  # will change for ,id name in form feilds, can see in view page source
    # lg = Login(auto_id=True)

    return render(request,'student/login.html',{'login':lg})