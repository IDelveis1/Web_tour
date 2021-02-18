from django.shortcuts import render
from random import shuffle
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from django.views import View
from .models import Task
import data
Tours = data.tours

def index(request):
    random_tours = list(range(1, 17))
    shuffle(random_tours)
    random_tours = random_tours[:6]
    lst_of_tours = [{**Tours.get(num), **{"id": num}} for num in random_tours]
    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'random_tours': lst_of_tours
    }
    return render(request, 'tours/index.html', context=context)

class DepartureView(View):
    template_name = 'tours/departure.html'
    def get(self, request, departure="msk"):
        if departure not in data.departures:
            raise Http404
        else:
            random_tours = list(range(1, 17))
            lst_of_tours = [{**Tours.get(num), **{"id": num}} for num in random_tours if Tours[num]["departure"] == departure]
            context = {
                'departure': departure,
                'tours': lst_of_tours
            }
            return render(request, self.template_name, context=context)

class TourView(View):
    template_name = 'tours/tours.html'

    def get(self, request, id=1):
        if id not in Tours:
            raise Http404
        else:
            return render(request, self.template_name, context=Tours[id])


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то пошло не так')

