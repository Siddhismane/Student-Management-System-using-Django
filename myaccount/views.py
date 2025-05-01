from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from student.models import Student_details
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        un=request.POST.get('un')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                messages.error(request,'Username already exists!')
                return redirect('sign_up')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email aready exists!')
                    return redirect('sign_up')
                else:
        
                    user=User.objects.create_user(first_name=fn,last_name=ln,username=un,email=email,password=pass1)
                    user.save()
                    messages.success(request,'Signed up successfully!')
                    return redirect('login')
        else:
            messages.error(request,'Password does not match!')
            return redirect('sign_up')


    return render(request,'myaccount/sign_up.html')

def login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pass1=request.POST.get('pass1')
        user=auth.authenticate(username=un,password=pass1)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'login successfully!')
            return redirect('dashboard')
        else:
            messages.success(request,'username or password is not valid!')
            return redirect('login')
    
    return render(request,'myaccount/login.html')

def logout(request):
    auth.logout(request)
    return redirect ('login')

def dashboard(request):
    data=Student_details.objects.order_by('name')
    context={
        'students': data

    }
    return render(request,'myaccount/dashboard.html',context)

def singlestudentdetails(request,reg_no):
    student=Student_details.objects.get(reg_no=reg_no)
    context={
        'student':student
    }

    if request.method=='POST':
       name=request.POST.get('name')
       city=request.POST.get('city')
       email=request.POST.get('email')
       course=request.POST.get('course')
       degree=request.POST.get('degree')
       persentage=request.POST.get('percentage')
       fee=request.POST.get('fee')
       student=Student_details.objects.get(reg_no=reg_no)
       student.name=name
       student.city=city
       student.email=email
       student.course=course
       student.degree=degree
       student.percentage=persentage
       student.fee=fee
       student.save()
       return redirect('dashboard')

    return render(request,'myaccount/singlestudentdetails.html',context)

def delete(request,reg_no):
    student=Student_details.objects.get(reg_no=reg_no)
    student.delete()
    return redirect('dashboard')



    