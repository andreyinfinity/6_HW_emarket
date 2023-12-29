from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views import generic
from catalog.models import Product
from product.forms import ProductForm, VersionForm
from product.models import Version
# CRUD для товаров


class ProductCreate(LoginRequiredMixin, generic.CreateView):
    """Класс добавления товара в БД"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_form.html'
    login_url = 'users:login'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductList(LoginRequiredMixin, generic.ListView):
    """Класс отображения страницы с товарами"""
    model = Product
    template_name = 'product/product_list.html'
    login_url = 'users:login'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Для вывода активной версии продукта в шаблон"""
        context_data = super().get_context_data(**kwargs)
        # Цикл по всем продуктам из списка
        for product in context_data['object_list']:
            # Получаем объект версий, если есть active True
            active_ver = product.version_set.filter(is_active=True).first()
            if active_ver:
                # Продукту добавляем поля с версией
                product.ver_num = active_ver.num
                product.ver_name = active_ver.name
            else:
                product.ver_num = None
                product.ver_name = None
        return context_data


class ProductUpdate(LoginRequiredMixin, generic.UpdateView):
    """Класс изменения товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_form.html'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        """Формсет для отображения формы версий продуктов при редактировании продукта"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Валидация формсета и проверка условия не более 1й активной версии"""
        formset = self.get_context_data()['formset']
        self.object = form.save(commit=False)
        if formset.is_valid():
            formset.save(commit=False)
            formset.instance = self.object
            # if not valid_active_version(formset.cleaned_data):
            #     context = {'formset': formset,
            #                'form': form,
            #                'error': 'Выберите не более 1 активной версии продукта!'}
            #     return render(self.request, 'product/product_form.html', context)
            formset.save()
        return super().form_valid(form)


class ProductDelete(LoginRequiredMixin, generic.DeleteView):
    """Класс удаления товара"""
    model = Product
    success_url = reverse_lazy('product:list')
    template_name = 'product/product_confirm_delete.html'
    login_url = 'users:login'


class VersionCreate(LoginRequiredMixin, generic.CreateView):
    """Класс добавления товара в БД"""
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('product:list_ver')
    login_url = 'users:login'

    def form_valid(self, form):
        """Метод для задания активной версии продукта, активность других
        версий этого продукта устанавливается в False"""
        if form.is_valid():
            if form.cleaned_data.get('is_active'):
                product_pk = form.cleaned_data.get('product').pk
                Version.objects.filter(product=product_pk).filter(is_active=True).update(is_active=False)
        form.save()
        return super().form_valid(form)


class VersionList(LoginRequiredMixin, generic.ListView):
    """Класс отображения страницы с товарами"""
    model = Version
    login_url = 'users:login'


class VersionUpdate(LoginRequiredMixin, generic.UpdateView):
    """Класс изменения товара"""
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('product:list_ver')
    login_url = 'users:login'

    def form_valid(self, form):
        """Метод для задания активной версии продукта, активность других
        версий этого продукта устанавливается в False"""
        if form.is_valid():
            if form.cleaned_data.get('is_active'):
                product_pk = form.cleaned_data.get('product').pk
                Version.objects.filter(product=product_pk).filter(is_active=True).update(is_active=False)
        form.save()
        return super().form_valid(form)


class VersionDelete(LoginRequiredMixin, generic.DeleteView):
    """Класс удаления товара"""
    model = Version
    success_url = reverse_lazy('product:list_ver')
    login_url = 'users:login'


# def valid_active_version(cleaned_data):
#     """Функция проверки количества активных версий в формсете"""
#     n = 0
#     for data in cleaned_data:
#         if data.get('is_active'):
#             n += 1
#             if n > 1:
#                 return False
#     return True
#
