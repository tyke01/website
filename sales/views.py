from django.shortcuts import render
from django.views.generic import ListView
from .models import Sales

# Create your views here.
def home_view(request):
    return render(request, 'sales/home.html', {})


class SalesListView(ListView):
    model= Sales
    template_name='sales/main.html'