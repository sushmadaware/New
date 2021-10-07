from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import StudentModel
from .forms import StudentModelForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Home(View):
    def get(self,request):
        context={}
        template_name='app1/home.html'
        return render(request,template_name,context)


class Create(View):
    def get(self,request):
        form=StudentModelForm()
        context={'form':form}
        template_name='app1/create.html'
        return render(request,template_name,context)

    def post(self,request):
        if request.method=='POST':
            form=StudentModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('read')

class Read(View):
    def get(self,request):
        obj=StudentModel.objects.all()
        context={'obj':obj}
        template_name='app1/read.html'
        return render(request,template_name,context)

class Update(View):
    def get(self,request,id):
        obj=StudentModel.objects.get(id=id)
        form=StudentModelForm(instance=obj)
        context={'form':form}
        template_name='app1/create.html'
        return render(request,template_name,context)

    def post(self,request,id) :
        obj=StudentModel.objects.get(id=id)
        if request.method=='POST':
            form=StudentModelForm(request.POST,instance=obj)
            if form.is_valid():
                 form.save()
                 return redirect('read')   

class Delete(View):
    def get(self,request,id):
        obj=StudentModel.objects.get(id=id)
        obj.delete()
        return redirect('read')                 

class Log_In(View):
    def get(self,request):
        template_name='app1/login.html'
        context={}
        return render(request,template_name,context)

    def post(self,request):
        if request.method=='POST':
            u=request.POST.get('uname')
            p=request.POST.get('pwd')
            user=authenticate(username=u,password=p)
            if user is not None:
                login(request,user)
                return redirect('create')
            else:
                messages.Error(request,'Invalid data')


class Log_Out(View):
    def get(self,request):
        logout(request)
        return redirect('home')


class Register(View):
    def get(self,request):
        form=UserCreationForm()
        context={'form':form}
        template_name='app1/register.html'
        return render(request,template_name,context)
        
    def post(self,request):
        form=UserCreationForm()
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
