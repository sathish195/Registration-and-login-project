from django.shortcuts import render
from django.views import View
from .models import Reg
from .forms import RegForm,LoginForm
from django.http import HttpResponse
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        r_f=RegForm()
        return render(request,'reg.html',{'reg_form':r_f})
class RegInsert(View):
    def post(self,request):
        r_f=RegForm(request.POST)
        if r_f.is_valid():
            r_f.save()
            return HttpResponse("registration successfull")
class LoginInput(View):
    def get(self,request):
        l_f=LoginForm()
        return render(request,'login.html',{'login_form':l_f})
class LoginView(View):
    def post(self,request):
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            user =MyLoginForm.cleaned_data['User_Name']
            passw=MyLoginForm.cleaned_data['Password']
            dbuser = Reg.objects.filter(User_Name=user,password=passw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return HttpResponse('login success')



