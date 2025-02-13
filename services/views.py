from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm, RegisterForm

# Home Page
def home(request):
    return HttpResponse("<h1>Welcome to the Gas Utility Service Portal</h1>")

# User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to login page
    else:
        form = RegisterForm()
    
    return render(request, 'services/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('service_request_list')  # Redirect to service request list
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'services/login.html')

# User Logout
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Redirect to login page

# Service Request List / Dashboard (Requires Login)
@login_required
def service_request_list(request):
    query = request.GET.get('q', '')  
    requests = ServiceRequest.objects.filter(name__icontains=query) if query else ServiceRequest.objects.all()

    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Service request submitted successfully!")
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()

    return render(request, 'services/dashboard.html', {'requests': requests, 'form': form, 'query': query})
