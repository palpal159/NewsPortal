from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from .models import Post, Author, User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostList(ListView):
    model = Post
    ordering = ['-post_date']
    template_name = 'post.html'
    context_object_name = 'posts'
    paginate_by = 5  # вот так мы можем указать количество записей на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostSearch(ListView):
    model = Post
    ordering = ['-post_date']
    template_name = 'post_search.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'onepost.html'
    context_object_name = 'posts'


class NewsCreate(CreateView, LoginRequiredMixin, TemplateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    permission_required = ('news.add_news', 'news.update_news')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get_or_created(user=user)[0]
            post.save()
            return self.form_valid(form)
        else:
            return self.form_valid(form)


class ArticlesCreate(CreateView, LoginRequiredMixin, TemplateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'
    permission_required = ('articles.add_articles', 'articles.update_articles')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.first()
            post.save()
            return self.form_valid(form)
        else:
            return self.form_valid(form)


# Добавляем представление для изменения товара.
class NewsUpdate(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'


class ArticlesUpdate(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')
