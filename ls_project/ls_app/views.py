# from turtle import title
from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import beats
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    all_beats = beats.objects.all().order_by('-rel_date').values()
    num_of_beats = beats.objects.all().count()
    paginator = Paginator(all_beats, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Live Sounds Records - Get Beats',
        'all_beats': all_beats,
        'num_of_beats': num_of_beats,
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)
  