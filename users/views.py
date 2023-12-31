import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserForm, RecoveryForm
from users.models import User


class RegisterView(generic.CreateView):
    """Представление регистрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            # деактивируем пользователя
            user.is_active = False
            # создаем и записываем код верификации
            verification_code = uuid.uuid4().hex
            user.uuid = verification_code
            user.save()
            # получаем домен сайта
            current_site = get_current_site(self.request)
            # создаем и отправляем письмо со ссылкой на активацию
            mail_subject = 'Ссылка для активации вашего аккаунта'
            message = (f"Для активации вашего аккаунта перейдите по ссылке:\n"
                       f"http://{current_site}{reverse_lazy('users:activate', args=[verification_code])}")
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(subject=mail_subject, body=message, to=[to_email], from_email=EMAIL_HOST_USER)
            email.send()

            return HttpResponse('Пожалуйста перейдите по ссылке, которая отправлена вам на электронную почту')
        return super().form_valid(form)


def activate(request, code):
    """Контроллер активации пользователя при переходе по ссылке из письма"""
    try:
        # поиск пользователя по uuid
        user = User.objects.get(uuid=code)
        # активация пользователя
        user.is_active = True
        user.uuid = None
        user.save()
        # при успешной активации редирект на страницу входа
        return HttpResponseRedirect(reverse_lazy('users:login'))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse('Ссылка для активации неверная!')


class UserUpdateView(generic.UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class RecoveryPassword(generic.CreateView):
    """Контроллер восстановления пароля"""
    model = User
    form_class = RecoveryForm
    template_name = 'users/recovery_password_form.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return HttpResponse('Пользователя с таким email не существует!')
        # генерация нового пароля и его запись
        new_pass = User.objects.make_random_password()
        user.set_password(new_pass)
        user.save()
        # создаем и отправляем письмо с новым паролем
        mail_subject = 'Вы запросили сброс пароля'
        message = (f"Ваш новый пароль\n"
                   f"{new_pass}")
        email = EmailMessage(subject=mail_subject, body=message, to=[email], from_email=EMAIL_HOST_USER)
        email.send()
        return HttpResponseRedirect(reverse_lazy('users:login'))
