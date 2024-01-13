from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Blog
# CRUD


class BlogCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Blog
    fields = ['title', 'message', 'preview']
    success_url = reverse_lazy('blog:blog_edit')
    permission_required = 'blog.add_blog'

    # def form_valid(self, form):
    #     """Метод записи в поле slug"""
    #     if form.is_valid():
    #         new_article = form.save()
    #         # Через request передаем недостающую форму slug
    #         # Для работы с кириллицей установлен pytils
    #         new_article.slug = slugify(self.request.POST.get('title'))
    #         # Сохраняем в БД
    #         new_article.save()
    #     return super().form_valid(form)


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        """Метод для отображения записей с пометкой видимый сортировка по дате"""
        queryset = super().get_queryset()
        return queryset.filter(visibility=True).order_by('-date')


class BlogEditListView(PermissionRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'blog/blog_edit_list.html'
    permission_required = 'blog.change_blog'


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Метод увеличения количества просмотров"""
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()

        if self.object.viewed == 100:
            # Отправка письма по достижении 100 просмотров
            send_mail(
                subject='Поздравляю!',
                message='Вы набрали 100 просмотров',
                from_email='aapot@yandex.ru',
                recipient_list=['aapot@ya.ru'],
                fail_silently=False
            )
        return self.object


class BlogUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Blog
    fields = ['title', 'message', 'preview']
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        """Переопределение метода для работы со slug"""
        return reverse_lazy('blog:view', kwargs={'slug': self.object.slug})


class BlogDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_edit')
    permission_required = 'blog.delete_blog'


def toggle_visibility(request, pk):
    """Контроллер изменения состояния видимости статьи"""
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.visibility:
        blog_item.visibility = False
    else:
        blog_item.visibility = True
    blog_item.save()
    return redirect(reverse_lazy('blog:blog_edit'))
