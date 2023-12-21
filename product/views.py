from django.urls import reverse_lazy
from django.views import generic
from catalog.models import Product
from product.forms import ProductForm
# CRUD для товаров


class ProductCreate(generic.CreateView):
    """Класс добавления товара в БД"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_form.html'


class ProductList(generic.ListView):
    """Класс отображения страницы с товарами"""
    model = Product
    template_name = 'product/product_list.html'


class ProductUpdate(generic.UpdateView):
    """Класс изменения товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_form.html'


class ProductDelete(generic.DeleteView):
    """Класс удаления товара"""
    model = Product
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_confirm_delete.html'
