from django.urls import path, include
from .views import SignUpView
from . import views

urlpatterns = [ #Patrón URL
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
]