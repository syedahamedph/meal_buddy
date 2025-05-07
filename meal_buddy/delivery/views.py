from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
# Create your views here.
def index(request):
    return render(request,'delivery/index.html')
def open_signin(request):
    return render(request,'delivery/signin.html')
def open_signup(request):
    return render(request,'delivery/signup.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        try:
            Customer.objects.get(username = username)
            return HttpResponse("DUPLICATE USER")
        except:
             Customer.objects.create(
                username = username,
                password = password,
                email = email,
                mobile = mobile,
                address = address,
            )
    return render(request, 'delivery/signin.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            Customer.objects.get(username = username, password = password)
            if username == 'admin':
                return render(request,'delivery/admin_home.html')
            else:
                return render(request,'delivery/customer_home.html')
                
    
        except Customer.DoesNotExist:
            return render(request,'delivery/fail.html')
        

def open_add_restaurant(request):
    return render(request,'delivery/add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name=request.POST.get('name'),
        picture=request.POST.get('picture'),
        cuisine=request.POST.get('cuisine'),
        rating=request.POST.get('rating'),

