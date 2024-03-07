from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .form import formz,formz2,formz3
from .models import Login
from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):
#
#     # if not request.user.is_authenticated:
#        form1 = formz()
#        if request.method == 'POST':
#            # form1 = AuthenticationForm(request=request,data=request.POST)
#            form1 = formz(request.POST)
#            if form1.is_valid():
#                form1.save()
#                return redirect("home_page")
#            #     if user is not None:
#            #         login(request,user)
#            #         return redirect("login")
#            #     else:
#            #         form1=AuthenticationForm()
#            # else:
#            #     return redirect("login")
#        return render(request,"login.html",context={'form': form1})
# #
def login(request):
    form1 = formz()
    if request.method == 'POST':
        form1 = formz(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home_page')
    return render(request,"login.html",context={'form': form1})

def registration(request):
    form2 = formz2()
    if request.method == 'POST':
        form2 = formz2(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("login")
    return render(request,"register.html",context={'form': form2})
    # if request.method == 'POST':
    #     form2 = formz2(request.POST)
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # if len(password) < 3:
    #     messages.error(request, 'Password must be at least 3 characterd')
    #     return redirect('register')
    # get_all_users_by_username = email.objects.filter(email=email)
    # if get_all_users_by_username():
    #     messages.error(request, 'error,username already exist use another')
    # return redirect('register')

@login_required
def booking(request):
    form3 = formz3()
    if request.method == 'POST':
        form3 = formz3(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect("home_page")

        # else:
        #     return render(request,"booking.html",{'form':form3})
    return render(request,"booking.html",context={'form':form3})
@login_required
def home_page(request):
    return render(request,"miniProject.html")



@login_required
def doctors(request):
    return render(request, "doctors.html")

def doct1(request):
    return render(request,"doct1.html")
def doct2(request):
    return render(request,"doct2.html")
def doct3(request):
    return render(request,"doct3.html")
def doct4(request):
    return render(request,"doct4.html")
def doct5(request):
    return render(request,"doct5.html")
def doct6(request):
    return render(request,"doct6.html")