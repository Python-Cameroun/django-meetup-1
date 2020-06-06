
from .views import *
from django.urls import path, re_path

urlpatterns = [
    
    path('index/', IndexView.as_view(), name="index"),    
    
    re_path(r'(?P<page>[a-z0-a\-/]+\.html?)$', DefaultHandlerView.as_view(), name="defaut_handler"),
]
