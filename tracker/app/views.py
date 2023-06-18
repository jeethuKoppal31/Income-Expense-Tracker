from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EntryForm
from .models import Entry
from django.utils import timezone
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request, "Account created successfully. You can now login.")
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def home(request):
    print(123)
    if request.method == 'POST':
        
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        entry_type = request.POST.get('entry_type')


        print('Description:', description)  # Add these lines
        print('Amount:', amount)
        print('Entry Type:', entry_type)

        entry = Entry(description=description, amount=amount, entry_type=entry_type)
        entry.save()
        return redirect('entry_list')
    
    return render(request, 'home.html')

def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.created_at = timezone.now()
            entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'create_entry.html', {'form': form})

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'entry_list.html', {'entries': entries}) 
    
    

def entry_edit_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if entry.user != request.user:
        # Handle unauthorized access here (e.g., display an error message)
        return redirect('entry_list')

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')  # Redirect to the entry list page
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry_edit.html', {'form': form})

def entry_delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if entry.user != request.user:
        # Handle unauthorized access here (e.g., display an error message)
        return redirect('entry_list')

    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')  # Redirect to the entry list page

    return render(request, 'entry_delete.html', {'entry': entry})

def LogoutPage(request):
    logout(request)
    return redirect('login')
