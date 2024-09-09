from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInLine(admin.TabularInline): #Permitiendo publicar un comentario
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin): #Permitiendo publicar un artículo
    inlines = [
        CommentInLine,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)