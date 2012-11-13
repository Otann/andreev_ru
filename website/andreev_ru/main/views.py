from django import http
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import check_for_language
from andreev_ru import settings

from andreev_ru.main.models import Work, Category, Person, Department

def prepare_base():
    return {}

def home(request):
    context = {
        'works': Work.objects.all(),
        'is_main': True,
        'debug': settings.PROJECT_ROOT
    }
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def works(request):

    category_id = request.GET.get('category', '1')
    category = Category.objects.get(pk=category_id)

    context = {
        'categories': Category.objects.all(),
        'category': category,
        'category_works': Work.objects.filter(categories__in=category_id)
    }

    return render_to_response('works.html', context, context_instance=RequestContext(request))
    
def work(request, slug):
    context = {
        'work': get_object_or_404(Work, slug=slug)
    }
    return render_to_response('work.html', context, context_instance=RequestContext(request))

def team(request):
    all_persons = Person.objects.all()
    all_positions = Department.objects.all()

    team = map(lambda position: (position, filter(lambda person: person.position == position, all_persons)), all_positions)
    context = {
        'team': team
    }
    return render_to_response('team.html', context, context_instance=RequestContext(request))

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