from django.shortcuts import render, redirect

from shop.models import Wine, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms


def home(request):
    wines = Wine.objects.all()
    categories = Category.objects.all()

    context = {
        "wines": wines,
        'categories': categories
    }
    return render(request, 'Shop/home.html', context)


def about(request):
    return render(request, 'Shop/about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged')
            return redirect('home')
        else:
            messages.success(request, 'There was an error, please try again')
            return redirect('login')
    else:
        return render(request, 'Shop/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, f'User has been updated')
            return redirect('home')
        else:
            return render(request, 'Shop/update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'You are not logged in')
        return redirect('login')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Your account {username} is registered successfully')
            return redirect('home')
        else:
            messages.success(request, f'There was a problem, Please try again')
            return redirect('register')

    return render(request, 'Shop/register.html', {'form': form})


def wine(request, pk):
    current_wine = Wine.objects.get(id=pk)

    context = {
        'wine': current_wine
    }

    return render(request, 'Shop/wine.html', context)


def category(request, pk):
    # Replaces dash with white space
    pk = pk.replace("-", ' ')
    try:
        current_category = Category.objects.get(name=pk)
        wines = Wine.objects.filter(category=current_category)
        context = {
            "wines": wines,
            "category": current_category
        }
        return render(request, 'Shop/category.html', context)
    except:
        messages.success(request, f'{pk} does not exist')
        return redirect('home')


def category_summery(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'Shop/category_summert.html', context)

