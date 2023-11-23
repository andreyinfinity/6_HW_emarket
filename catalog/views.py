from django.shortcuts import render
from django.views import generic

from .forms import ProductForm
from .models import Product, Contacts

# Create your views here.


def index(request):
    """Функция отображения главной страницы"""
    new_products = Product.objects.order_by('-date_modification')[:4]
    print(new_products)
    top_items = Product.objects.order_by('-viewed')[:4]
    return render(request=request, template_name='catalog/home.html',
                  context={'new_products': new_products,
                           'top_items': top_items,
                           'title': 'Provision&Co'})


def contacts(request):
    """Функция отображения страницы контактов"""
    cont = Contacts.objects.get()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, email: {email}. {message}')
    return render(request=request, template_name='catalog/contacts.html',
                  context={'contacts': cont,
                           'title': 'Контакты'})


class ProductView(generic.DetailView):
    """Класс отображения карточки товара"""
    model = Product
    template_name = 'catalog/product.html'


class CatalogView(generic.ListView):
    """Класс отображения каталога товаров с пагинацией"""
    model = Product
    template_name = 'catalog/catalog.html'
    paginate_by = 8


class ProductAdd(generic.CreateView):
    """Класс добавления товара в БД"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add.html'
    success_url = '/added'


class ProductAdded(generic.TemplateView):
    """Класс отображения страницы успешного добавления товара"""
    model = Product
    template_name = 'catalog/added.html'
