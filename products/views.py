from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
def home(request):
  return render(request, 'products/home.html')

def user_login(request):
   if request.method == 'POST':
     form = LoginForm(request.POST)
     if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(
          request,
          username=cd['username'],
          password=cd['password']
          )
        if user is not None:
           if user.is_active:
             login(request, user)
             return redirect('home')
           else:
             return HttpResponse('Disabled account')
        else:
           return HttpResponse('Invalid login')
   else:
     form = LoginForm()
     return render(request,'products/login.html', {'form': form}) 

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(
      user_form.cleaned_data['password']
      )
      new_user.save()
      return render(
      request,
      'products/register_done.html',
      {'new_user': new_user}
      )
  else:
    user_form = UserRegistrationForm()
  return render(
    request,
    'products/register.html',
    {'user_form': user_form}
    )

