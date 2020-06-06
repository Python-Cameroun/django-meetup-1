
from .views import *
from django.urls import path, re_path

urlpatterns = [
    
    path('index/', HotelListView.as_view(), name="index"),    
    path('<str:shortname>/', HotelView.as_view(), name='hotel'),
    
    re_path(r'(?P<page>[a-z0-a\-/]+\.html?)$', DefaultHandlerView.as_view(), name="defaut_handler"),
]
