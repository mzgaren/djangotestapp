from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddReportForm
from .models import Report
# Create your views here.


def index(request):
    return render(request, 'index.html', {})

def home(request):
    reports = Report.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in !")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in please try again ")
            return redirect('home')
    else:
        return render(request, 'home.html', {'reports': reports})


def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out ! ")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have been loged In")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def employee_report(request, pk):
    if request.user.is_authenticated:
        employee_report = Report.objects.get(id=pk)
        return render(request, 'report.html', {'employee_report': employee_report})
    else:
        messages.success(request, "you must Be logged In to view reports")
        return redirect('home')


def delete_report(request, pk):
    if request.user.is_authenticated:
        delete_it = Report.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Report has been deleted !")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete reports")
        return redirect('home')


def add_report(request):
    form = AddReportForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                task_list = form.save(commit=False)
                task_list.user_name = request.user 
                task_list.save()
                messages.success(request, "Report added successfuly ! ")
                return redirect('home')
        return render(request, 'add_report.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to delete reports")
        return redirect('home')

def update_report(request, pk):
    form = AddReportForm(request.POST)
    if request.user.is_authenticated:
        current_report = Report.objects.get(id=pk)
        form = AddReportForm(request.POST or None, instance=current_report)
        if form.is_valid():
                form.save()
                messages.success(request, "Report Updated successfuly ! ")
                return redirect('home')
        return render(request, 'update_report.html', {'form': form })
    else:
        messages.success(request, "You must be logged in to delete reports")
        return redirect('home')