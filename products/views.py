from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, ReviewForm, UserEditForm, ContactForm
from .models import Device, Category, Review
from django.contrib.auth.decorators import login_required
from .models import Device
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Device, Wishlist, StoreLink
from django.contrib import messages
from .models import Cart
#Home page
def home(request):
    categories = Category.objects.all()
    devices = list(Device.objects.all())

    # Sort devices by average rating (highest first)
    devices.sort(
        key=lambda x: x.average_rating(),
        reverse=True
    )
    # Take only the top 3
    best_devices = devices[:3]
    return render(
        request,
        "products/home.html",
        {
            "categories": categories,
            "best_devices": best_devices,
        },
    )

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

    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')

    if query:
        devices = Device.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        devices = Device.objects.all()

    # Sorting
    if sort == "az":
        devices = devices.order_by("name")

    elif sort == "za":
        devices = devices.order_by("-name")

    elif sort == "low":
        devices = devices.order_by("price")

    elif sort == "high":
        devices = devices.order_by("-price")

    return render(request, 'products/device_list.html', {
        'devices': devices,
        'query': query,
        'sort': sort,
    })

#Device Details
def device_detail(request, id):

    device = get_object_or_404(Device, id=id)
    reviews = Review.objects.filter(device=device)
    store_links = device.store_links.all().order_by('price')
    similar_devices = Device.objects.filter(
    category=device.category).exclude(id=device.id)
    preview_devices = similar_devices[:3]
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

    # Wishlist check
    is_wishlisted = False

    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            device=device
        ).exists()
    is_in_cart = False
    if request.user.is_authenticated:
        is_in_cart = Cart.objects.filter(
        user=request.user,
        device=device
    ).exists()

    return render(
        request,
        'device_detail.html',   # or 'products/device_detail.html'
        {
            'device': device,
            'reviews': reviews,
            'review_form': review_form,
            'is_wishlisted': is_wishlisted,
            'store_links': store_links,
            'preview_devices': preview_devices,
            'similar_count': similar_devices.count(),
            'is_in_cart': is_in_cart,
        }
    )

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

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related('device')
    cart_items = Cart.objects.filter(
    user=request.user
)

    return render(
        request,
        "products/profile.html",
        {
            "wishlist_items": wishlist_items,
            'cart_items': cart_items,
            
        }
    )

#Profile Edit
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

#Adding product in wishlist
@login_required
def toggle_wishlist(request, id):
    device = get_object_or_404(Device, id=id)
    item, created = Wishlist.objects.get_or_create(
        user=request.user,
        device=device
    )
    if not created:
        item.delete()
    return redirect('device_detail', id=device.id)

#My Wishlist
@login_required
def my_wishlist(request):
    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related('device')
    return render(
        request,
        "products/my_wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )

#Edit Review
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )
    if request.method == "POST":
        form = ReviewForm(
            request.POST,
            instance=review
        )
        if form.is_valid():
            form.save()
            return redirect(
                "device_detail",
                id=review.device.id
            )
    else:
        form = ReviewForm(instance=review)
    return render(
        request,
        "products/edit_review.html",
        {
            "form": form,
            "review": review
        }
    )

#About us
def about(request):
    return render(request, "products/about.html")

#Contact us
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully!"
            )
            return redirect("contact")
    else:
        form = ContactForm()
    return render(
        request,
        "products/contact.html",
        {
            "form": form
        }
    )
@login_required
def toggle_cart(request, device_id):

    device = get_object_or_404(Device, id=device_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        device=device
    )

    if not created:
        cart_item.delete()

    return redirect('device_detail', device.id)
from .models import Cart
from django.contrib.auth.decorators import login_required


@login_required
def my_cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    return render(
        request,
        'my_cart.html',
        {
            'cart_items': cart_items
        }
    )