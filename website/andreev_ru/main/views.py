from datetime import datetime
import json

from django import http
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import check_for_language
from django.core.urlresolvers import reverse

from andreev_ru import settings
from andreev_ru.main.models import Work, Category, Person, Department, CustomPage
from andreev_ru.settings import MEDIA_URL


def prepare_base():
    return {}

def home(request):
    context = {
        'works': Work.objects.all(),
        'is_main': True,
    }
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def works(request):

    categories = []
    for cat in Category.objects.all():
        categories.append((cat, Work.objects.filter(categories__in=str(cat.id)).count()))

    try:
        category_id = request.GET.get('category', '0')
        category = Category.objects.get(pk=category_id)
        works = Work.objects.filter(categories__in=category_id)
    except ObjectDoesNotExist:
        category = { 'id': 0 }
        works = Work.objects.all()

    context = {
        'page': 'works',
        'total': Category.objects.count(),
        'categories': categories,
        'category': category,
        'category_works': works
    }

    return render_to_response('works.html', context, context_instance=RequestContext(request))

def work(request, slug):
    work = get_object_or_404(Work, slug=slug)
    more_amount = 5
    more_works = {}
    for item in Work.objects.order_by('?').exclude(id=work.id).filter(categories__in=work.categories.all())[:more_amount]:
        more_works[item.id] = item

    # if works in same categories is not enough
    if len(more_works) < more_amount:
        for item in Work.objects.exclude(id=work.id).order_by('?')[:more_amount-len(more_works)]:
            more_works[item.id] = item

    context = {
        'page': 'works',
        'work': work,
        'more_works': more_works.values()
    }
    return render_to_response('work.html', context, context_instance=RequestContext(request))

def page(request, slug):
    context = {
        'page': get_object_or_404(CustomPage, slug=slug)
    }
    return render_to_response('page.html', context, context_instance=RequestContext(request))

def team(request):
    all_persons = Person.objects.all()
    all_positions = Department.objects.all()

    team = map(lambda position: (position, filter(lambda person: person.position == position, all_persons)), all_positions)
    context = {
        'page': 'team',
        'team': team
    }
    return render_to_response('team.html', context, context_instance=RequestContext(request))

def search(request):
    context = {
        'page': 'team',
    }
    return render_to_response('search.html', context, context_instance=RequestContext(request))

def search_json(request):
    query = request.REQUEST.get('query', None).lower()
    lang  = request.LANGUAGE_CODE
    result = []
    if query:
        works = {}
        #TODO: more elegance with lang
        for work in Work.objects.filter(**{'title_' + lang + '__icontains': query}):
            works[work.id] = work
        for work in Work.objects.filter(**{'description_' + lang + '__icontains': query}):
            works[work.id] = work

        for work in works.values():
            result.append({
                'href':    'works/' + work.slug, #TODO: reverse('andreev_ru.main.views.works', args=(work.slug,)),
                'image':   work.images.all()[0].image.url if work.images.count() > 0 else '',
                'heading': work.title,
                'content': ' '.join(work.description.split(' ')[:15]) + '...'
            })

        for person in Person.objects.filter(**{'name_' + lang + '__icontains': query}):
            result.append({
                'href':    'persons/#%d' % person.id,
                'image':   person.image.url,
                'heading': person.name,
                'content': ' '.join(person.bio.split(' ')[:15]) + '...'
            })

    return HttpResponse(json.dumps(result), mimetype="application/json")