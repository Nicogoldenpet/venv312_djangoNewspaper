from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import CommentForm

# Create your views here.
class CommentGet(LoginRequiredMixin, DetailView): #Creando la vista para ver comentarios (El usuario deberá loguearse)
    model = Article
    template_name = "article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

class CommentPost(SingleObjectMixin, FormView): #Creando la vista para publicar comentarios (El usuario deberá loguearse)
    model = Article
    form_class = CommentForm
    template_name = "article_details.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object ()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_details", kwargs={"pk": article.pk})

class ArticleListView(LoginRequiredMixin, ListView): #Creando la vista para ver la lista de artículos (El usuario deberá esta logueado)
    model = Article
    template_name = "article_list.html"

    
class ArticleDetailsView(LoginRequiredMixin, View): #Creando la vista para ver los detalles del artículo (El usuario deberá esta logueado)
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view() #Ver comentarios
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view() #Y postear comentarios
        return view(request, *args, **kwargs)
    
    
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Creando la vista para actualizar un artículo 
                                                                              # (El usuario deberá esta logueado)
                                                                              # (Si el texto no es del autor arrojara error 403 FORBIDDEN)
    model = Article
    fields = ( #Título y cuerpo
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Creando la vista para eliminar un artículo 
                                                                              # (El usuario deberá esta logueado)
                                                                              # (Si el texto no es del autor arrojara error 403 FORBIDDEN)
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    
class ArticleCreateView(LoginRequiredMixin, CreateView): # Creando la vista para eliminar un artículo (El usuario deberá esta logueado)
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)