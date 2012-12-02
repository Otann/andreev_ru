import json

from django import http
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import check_for_language
from django.core.urlresolvers import reverse

from andreev_ru import settings
from andreev_ru.main.models import Work, Category, Person, Department, CustomPage

def prepare_base():
    return {}

def home(request):
    context = {
        'works': Work.objects.all(),
        'is_main': True,
        'debug': reverse('redactor_upload_image', kwargs={'upload_to': ''})
    }
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def works(request):

    categories = []
    for cat in Category.objects.all():
        categories.append((cat, Work.objects.filter(categories__in=str(cat.id)).count()))

    try:
        category_id = request.GET.get('category', '1')
        category = Category.objects.get(pk=category_id)
        works = Work.objects.filter(categories__in=category_id)
    except ObjectDoesNotExist:
        category = None
        works = Work.objects.all()

    context = {
        'page': 'works',
        'categories': categories,
        'category': category,
        'category_works': works
    }

    return render_to_response('works.html', context, context_instance=RequestContext(request))

def work(request, slug):
    work = get_object_or_404(Work, slug=slug)
    more_amount = 5
    more_works = {}
    for item in Work.objects.order_by('?').filter(categories__in=work.categories.all())[:more_amount]:
        more_works[item.id] = item
    if len(more_works) < 5:
        for item in Work.objects.order_by('?')[:more_amount-len(more_works)]:
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

#todo(Anton): make this work: switch lang and redirect back to referrer or home
def set_lang(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response