
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from front.models import Hotel, Reservation, Gallery
from django.views.generic import ListView


class IndexView(TemplateView):
    template_name = "front/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add data to context
        return context
    
    
class HotelView(TemplateView):
    template_name = "front/hotel.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        short_name = self.kwargs.get('shortname')
        hotel = Hotel.objects.get(short_name=short_name)
        context['hotel'] = hotel
        
        galleries = hotel.galleries.all()
        print(galleries)
        
        rooms = galleries.filter(type='room')
        print('rooms', rooms)
        context['rooms'] = rooms
        # add data to context
        return context
    


class DefaultHandlerView(TemplateView):
    
    def get(self, *args, **kwargs):
        page = self.kwargs.get('page')
        self.template_name = "front/"+page
        return super().get(*args, **kwargs)

class HotelListView(ListView):
    model = Hotel
    template = "front/hotel-list.html"
