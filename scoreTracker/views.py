from django.shortcuts import render
from .forms import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect

from django.http import HttpResponse,HttpResponseRedirect
from .models import Ludo

def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        # form=AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     user=form.get_user()
        #     login(request,user)
            
        else:
            messages.info(request,"invalid credentials")
            return redirect("/login")
            # print("heyyy")
    else:
        form=AuthenticationForm()
        return render(request,'login.html', {'form': form})
    
    # c={'form':form}
    # c= c.update(csrf(request))
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')


def home(request):
    ludo=Ludo.objects.all().order_by('-Average','-TotalScore','MatchesPlayed')   
    return render(request,'test.html',{'ludo':ludo})

def addMatch(request):
    def savit(name,score):
        print(name)
        res=Ludo.objects.get(PlayerName=name)
        res.TotalScore+=score
        res.MatchesPlayed+=1
        res.Average=res.TotalScore/res.MatchesPlayed
        res.save()
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(PostForm)
        if form.is_valid():
            savit(form['First'].value(),10)
            savit(form['Second'].value(),5)
            savit(form['Third'].value(),0)
            savit(form['Fourth'].value(),0)
            form.save()
            if 'one' in request.POST:
                return HttpResponseRedirect(request.path_info)
            return redirect("/")
    else:
        form = PostForm()
    
    if request.user.is_authenticated:
        # print("yes")
        return render(request,'newMatch.html',{'form':form})
    else:
        return redirect("/login")
def addPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            if 'one' in request.POST:
                return HttpResponseRedirect(request.path_info)
            return redirect("/")

    else:
        form = PlayerForm()
    if request.user.is_authenticated:
        return render(request,'newPlayer.html')
    else:
            return redirect("/login")


def history(request):
    hist=History.objects.all()
    return render(request,'matchHistory.html',{'hist':hist})
