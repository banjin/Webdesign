from django.shortcuts import *
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from models import User

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)

def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username,password=password)
            print username,password
            return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
        return render_to_response('regist.html',{'uf':uf})

def login(request):
    if request.method =="POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users= User.objects.filter(username__exact=username,password__exact=password)
            if users:

                response= HttpResponseRedirect('/index/')

                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')

    else:
        uf = UserForm()
        return render_to_response('login.html',{'uf':uf})


def index(request):

    username = request.COOKIES.get('username','')

    return render_to_response('index.html',{'username':username})

def logout(request):
    #del request
    response = HttpResponse('logout')
    response.delete_cookie('username')
    return response

