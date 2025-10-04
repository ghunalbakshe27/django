from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from backend.models import customuser
User = customuser



def aboutus(request):
    return render(request, 'backend/aboutus.html')

def arjit(request):
    return render(request, 'backend/arjit.html')

def bhajan(request):
    return render(request, 'backend/bhajan.html')

def drivelist(request):
    return render(request, 'backend/drivelist.html')

def genres(request):
    return render(request, 'backend/genres.html')

def honeys(request):
    return render(request, 'backend/honeys.html')

def indianhits(request):
    return render(request, 'backend/indianhits.html')

def mixlist(request):
    return render(request, 'backend/mixlist.html')

def new_releases(request):
    return render(request, 'backend/new releases.html')
def phonk(request):
    return render(request, 'backend/phonk.html')

def punjabi_hits(request):
    return render(request, 'backend/punjabi hits.html')

def subh1(request):
    return render(request, 'backend/subh1.html')

def top(request):
    return render(request, 'backend/top.html')

def topeng(request):
    return render(request, 'backend/topeng.html')

def trend(request):
    return render(request, 'backend/trend.html')


@csrf_protect
def user_login(request):
    # """Handle user login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged out successfully!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password!')
            return render(request, 'backend/index.html')
    
    return render(request, 'backend/index.html')

@csrf_protect
def user_register(request):
    # """Handle user registration"""
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        
        # Split fullname into first_name and last_name
        name_parts = fullname.strip().split(' ', 1)  # Split only on first space
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        # Basic validation
        if not fullname.strip():
            messages.error(request, 'Full name is required!')
            return redirect('ogregister')
            
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('ogregister')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('ogregister')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('ogregister')
        
        try:
            # Create new user - THIS SAVES TO YOUR MYSQL DATABASE! 🔥
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)  # Hash the password
            user.save()
            
            messages.success(request, 'Registration successful! Please login with your credentials.')
            return redirect('user_login')
            
        except Exception as e:
            messages.error(request, 'Registration failed. Please try again.')
            return redirect('ogregister')
    return render(request, 'backend/ogregister.html')


def user_logout(request):
    # """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('user_login')

def homepage(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'backend/homepage.html')
