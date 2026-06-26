from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, ReviewForm, UserEditForm
from .models import Device, Category, Review
from django.contrib.auth.decorators import login_required


#Home page
def home(request):
    categories = Category.objects.all()
    return render(request,'products/home.html',{'categories': categories})

#Login
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

#Registration
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

#Device List
def device_list(request):
    devices = Device.objects.all()
    return render(
        request,
        'products/device_list.html',
        {'devices': devices}
    )

#Device Details
def device_detail(request, id):
    device = Device.objects.get(id=id)
    reviews = Review.objects.filter(device=device)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.device = device
            new_review.user = request.user
            new_review.save()
            return redirect('device_detail', id=device.id)
    else:
        review_form = ReviewForm()
    return render(request, 'device_detail.html', {'device': device, 'reviews': reviews, 'review_form': review_form})

#Category wise Device listing
def category_devices(request, category_id):
    category = Category.objects.get(id=category_id)

    devices = Device.objects.filter(
        category=category
    )

    return render(
        request,
        'products/device_list.html',
        {
            'devices': devices,
            'category': category
        }
    )

#Profile 
@login_required
def profile(request):
    return render(
        request,
        "products/profile.html"
    )

#Profile Edit
from django.contrib import messages

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserEditForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Profile updated successfully."
            )
            return redirect("profile")
    else:
        form = UserEditForm(
            instance=request.user
        )
    return render(
        request,
        "products/edit_profile.html",
        {"form": form}
    )

#MY Reviews Section
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user)

    return render(
        request,
        "products/my_reviews.html",
        {"reviews": reviews}
    )