from django.shortcuts import render
from .models import Product, Contacts

# Create your views here.


def index(request):
    new_products = Product.objects.order_by('-date_modification')[:4]
    print(new_products)
    top_items = Product.objects.order_by('-viewed')[:4]
    return render(request=request, template_name='home.html',
                  context={'new_products': new_products,
                           'top_items': top_items})


def contacts(request):
    cont = Contacts.objects.get()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, email: {email}. {message}')
    return render(request=request, template_name='contacts.html',
                  context={'contacts': cont})
