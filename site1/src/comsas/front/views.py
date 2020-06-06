
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "front/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add data to context
        return context
    


class DefaultHandlerView(TemplateView):
    
    def get(self, *args, **kwargs):
        page = self.kwargs.get('page')
        self.template_name = "front/"+page
        return super().get(*args, **kwargs)
