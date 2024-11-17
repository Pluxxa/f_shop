from django.shortcuts import render, redirect
from .models import Product
from .forms import UserRegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def product_list(request):
    products = Product.objects.filter(is_active=True).order_by('order', 'name')
    return render(request, 'flow_shop/product_list.html', {'products': products})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect("product_list")  # Перенаправляем на каталог
    else:
        form = UserRegistrationForm()
    return render(request, "flow_shop/register.html", {"form": form})