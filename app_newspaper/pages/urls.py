from django.urls import path
from .views import HomePageView

urlpatterns = [ #URL principal "home"
    path('', HomePageView.as_view(), name='home'),
]