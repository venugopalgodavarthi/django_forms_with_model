from django.http.response import HttpResponse
from django.shortcuts import render
from pro7.forms import registerform
from authe.models import registermodel
def sample(request):
    print(request)
    if request.method=='POST':
        res=request.POST['username']
        res1=request.POST['password']
        print(res,res1)
        print(request.POST)
        print(type(request.POST))
    return render(request,'sample.html')


def register(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['repassword']
        email=request.POST['email']
        phone=request.POST['phone']
        dob=request.POST['dob']
        gender=request.POST['gender']        
        print(user,pass1,pass2,email,phone,dob,gender,)
        if pass1==pass2:
            registermodel.objects.create(username=user,password=pass2,email=email,gender=gender,dob=dob,phone=phone)
        else:
            return HttpResponse('password is incorrect')
    if request.method=='get':
        form=registerform()
    return render(request,'register.html',{'form':form})

def details(request):
    res=registermodel.objects.all()
    return render(request,'details.html',{'res':res})

def sdetails(request):
    res=False
    if request.method=='POST':
        email=request.POST['email']
        res= registermodel.objects.filter(email=email)
    form=registerform()
    return render(request,'sdetails.html',{'form':form,'res':res})
