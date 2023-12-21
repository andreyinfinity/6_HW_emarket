from django.views import generic
from .forms import FeedbackForm
from .models import Product, Contacts, Feedback


class IndexView(generic.TemplateView):
    """Класс отображения главной страницы
    переопределен метод context для получения последних 4-х продуктов и топ 4 продуктов"""
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        """Метод для отображения списков продуктов, отсортированных по дате и просмотрам"""
        context = super().get_context_data()
        context['new_products'] = Product.objects.order_by('-date_modification')[:4]
        context['top_items'] = Product.objects.order_by('-viewed')[:4]
        context['title'] = 'Provision&Co'
        return context


class ContactsCreateView(generic.CreateView):
    """Класс получения контактной информации от посетителя. Выводится модель Contacts и создается форма Feedback"""
    model = Feedback
    form_class = FeedbackForm
    template_name = 'catalog/contacts.html'
    success_url = '/contacts'

    def get_context_data(self, **kwargs):
        """Вывод контактной информации из модели Contacts"""
        context = super().get_context_data()
        context['contacts'] = Contacts.objects.get()
        context['title'] = 'Контакты'
        return context


class ProductDetailView(generic.DetailView):
    """Класс отображения подробной информации о товаре и список
    топ товаров по просмотрам в этой же категории"""
    model = Product
    template_name = 'catalog/product.html'

    def get_object(self, queryset=None):
        """Метод увеличения количества просмотров"""
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        """Метод вывода товаров из той же категории сортированный по просмотрам"""
        context = super().get_context_data(**kwargs)
        same_products = Product.objects.filter(
            category=self.object.category).exclude(pk=self.object.pk).order_by('-viewed')[:4]
        context['same_products'] = same_products
        return context


class CatalogView(generic.ListView):
    """Класс отображения каталога товаров с пагинацией"""
    model = Product
    template_name = 'catalog/catalog.html'
    paginate_by = 8

