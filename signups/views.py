from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def join(request):
    if request.method == 'POST':
            username = request.POST.get('_id')
            password = request.POST.get('_pw')
            password2 = request.POST.get('_pwre')
            if password != password2 :
                state = "비번 틀림 좆만아! ㅎ"
            else :
                email = request.POST.get('_email')
                state = "Signup!"
                try :
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return HttpResponseRedirect('../')
                except :
                    state = 'ID Exists!'
    return render_to_response("join.html", locals(), RequestContext(request))

def index(request):
    loggedin = False
    if request.user.is_authenticated():
        state = "Welcome, " + request.user.username
        loggedin = True
    else:
        state = "Tag me!"

    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'login' :
            username = request.POST.get('_id')
            password = request.POST.get('_pw')
            user = authenticate(username = username, password = password)
            if user is not None :
                if user.is_active:
                    login(request, user)
                    state = "Welcome, " + request.user.username
                    loggedin = True
                else :
                    state = '비활성화'
            else :
                state = 'Login Failed!'
        elif type == 'logout' :
            logout(request)
            state = 'Logged Out!'
            loggedin = False


    return render_to_response("index.html", locals(), RequestContext(request))

'''

from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth import authenticate, login
from .models import SignUp, SignUpForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    state = "ABCZ"
    if request.POST:
        type = request.POST.get('type')
        if type == 'login' :
            username = request.POST.get('_id')
            pw1 = request.POST.get('_pw')
            try:
                lastboy = SignUp.objects.get(_id =username)
                pw2 = lastboy._pw
                if pw1 == pw2:
                    state = "login successful"
                else:
                    state = "login try failed"
            except ObjectDoesNotExist:
                state = "no such ID"

        elif type == 'signup':
            #awegaweg
            newboyForm = SignUpForm(request.POST)
            if newboyForm.is_valid():
                newboyForm.save()
                state = "signup Successful"
            else:
                state = "signup try fail"
        """ user = authenticate(_id = username, _pw = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = 'Login Success'
            else :
                state = "Login Failed"
        else :
            state = "Username/Password were incorrect" """

    return render_to_response("index.html", locals(), RequestContext(request))

'''