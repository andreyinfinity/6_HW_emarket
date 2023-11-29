
# def index(request):
#     """Функция отображения главной страницы"""
#     new_products = Product.objects.order_by('-date_modification')[:4]
#     top_items = Product.objects.order_by('-viewed')[:4]
#     return render(request=request, template_name='catalog/home.html',
#                   context={'new_products': new_products,
#                            'top_items': top_items,
#                            'title': 'Provision&Co'})

# def contacts(request):
#     """Функция отображения страницы контактов"""
#     cont = Contacts.objects.get()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'Name: {name}, phone: {phone}, email: {email}. {message}')
#     return render(request=request, template_name='catalog/contacts.html',
#                   context={'contacts': cont,
#                            'title': 'Контакты'})


def product_view(request, pk):
    """Функция отображения подробной информации о товаре и список
    топ товаров по просмотрам в этой же категории"""
    try:
        product = Product.objects.get(pk=pk)
        Product.objects.filter(pk=pk).update(viewed=F('viewed') + 1)
        same_products = Product.objects.filter(category=product.category).exclude(pk=pk).order_by('-viewed')[:4]
    except Product.DoesNotExist:
        raise Http404("Товар не найден")
    context = {'product': product,
               'same_products': same_products}

    return render(request=request,
                  template_name='catalog/product.html',
                  context=context)


def category_view(request, pk):
    pass
