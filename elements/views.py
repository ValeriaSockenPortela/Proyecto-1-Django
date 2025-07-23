from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import request

from .forms import ElementForm
from .models import Element
# Create your views here.

def index(request):
    elements = Element.objects.all()
    paginator = Paginator(elements, 10)
    page_number = request.GET.get('page')
    return render(request, 'element/index.html', {'elements': paginator.get_page(page_number)})

def add(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            element = Element(
                title=cd['title'],
                slug=cd['slug'],
                description=cd['description'],
                price=cd['price'] or 0,
                type=cd['type'],
                category=cd['category']
            )
            element.save()
            return redirect('elements:index')
    else:
        form = ElementForm()

    return render(request, 'element/add.html', {'form': form})

