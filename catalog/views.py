from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request=request, template_name='catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, email: {email}. {message}')
    return render(request=request, template_name='catalog/contacts.html')
