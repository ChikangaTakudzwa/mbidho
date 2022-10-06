from django.shortcuts import render
""" Views """
from django.core.paginator import Paginator
from .models import Beats

# Create your views here.
def index(request):
    """ Index Page """
    all_beats = Beats.objects.all().order_by('-rel_date').values()
    num_of_beats = Beats.objects.all().count()
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
