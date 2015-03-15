import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Race
from forms import UpNextForm, CallRaceForm
from django.contrib.admin.views.decorators import staff_member_required

def results(request):

    results = {
        'up_next': False,
        'completed': [],
        'upcoming': [],
    }

    for race in Race.objects.all():

        race_obj = {
            'slug': race.slug,
            'name': race.name,
            'up_next': race.up_next,
            'results': race.results,
            'completed': race.completed,
            'url': race.url,
        }

        if race.up_next:
            results['up_next'] = race_obj
        elif race.completed:
            results['completed'].append(race_obj)
        else:
            results['upcoming'].append(race_obj)

    return HttpResponse(json.dumps(results), content_type="application/json")

@staff_member_required
def up_next(request):

    context = {}

    if request.method == 'POST':

        form = UpNextForm(request.POST)

        if form.is_valid():
            race = form.cleaned_data['race']

            Race.objects.all().update(up_next=False)

            race.up_next = True
            race.save()

            context['message'] = "The %s race is now the upcoming race." % race.name

    context['form'] = UpNextForm()

    return render(request, 'up_next.html', context)

@staff_member_required
def call_race(request):

    context = {}

    if request.method == 'POST':

        form = CallRaceForm(request.POST)

        if form.is_valid():
            race = form.cleaned_data['race']

            race.results = form.cleaned_data['results']
            race.completed = True
            race.save()

            context['message'] = "The %s race is now updated with the following results: %s." % (race.name, race.results)

    context['form'] = CallRaceForm()

    return render(request, 'call_race.html', context)
