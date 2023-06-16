from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            
            try:
                user = User.objects.create_user(username=uname, email=email, password=pass1)
                
                return HttpResponse("User created successfully!")
            except Exception as e:
                return HttpResponse(f"Error creating user: {str(e)}")
    else:
        return render(request, 'signup.html') 
