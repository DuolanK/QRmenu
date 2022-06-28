from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from django.contrib import messages

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы Успешно зарегистрировались!')
            return redirect ('shop:login')
        else:
            messages.error(request, 'Ошибка регистрации, ну тут наши полномочия всё')
    else:
        form = UserCreationForm()
    return render(request, 'shop/registration.html', {"form":form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:product_list')
    else:
        form = UserLoginForm
    return render(request, 'shop/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')