import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from easy_thumbnails.files import get_thumbnailer
from andreev_ru.main.templatetags.custom_tags import transliterate

from andreev_ru.main.models import *
from andreev_ru.settings import IMAGE_CROPPING_THUMB_SIZE


def prepare_base():
    return {}


def home(request):
    top_news = News.objects.filter(is_featured=True)[:1]
    if len(top_news) > 0:
        news = top_news[0]
        news_text = news.title
        # if len(news_text) < 60:
        #     news_text += u'. ' + news.content[:60-len(news_text)] + u'...'
    else:
        news_text = None
    context = {
        'icons': TimelineIcon.objects.all(),
        'news_text': news_text,
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
        category = {'id': 0}
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
        for item in Work.objects.exclude(id=work.id).order_by('?')[:more_amount - len(more_works)]:
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


def search_json(request):
    query = request.REQUEST.get('query', None).lower()
    lang = request.LANGUAGE_CODE
    result = []
    if query:
        works = {}

        for work in Work.objects.filter(**{'title_' + lang + '__icontains': query}):
            works[work.id] = work
        for work in Work.objects.filter(**{'description_' + lang + '__icontains': query}):
            works[work.id] = work

        for work in works.values():
            thumb_options = {
                'size': IMAGE_CROPPING_THUMB_SIZE,
                'box': work.thumb,
                'crop': True,
                'detail': True,
            }

            result.append({
                'href':    reverse('work', args=[work.slug]) + '#project',
                'image':   get_thumbnailer(work.image).get_thumbnail(thumb_options).url if work.image else '',
                'heading': work.title,
                'content': ' '.join(work.description.split(' ')[:15]) + '...'
            })

        for person in Person.objects.filter(**{'name_' + lang + '__icontains': query}):
            if lang == 'ru':
                name = person.name_ru
            else:
                name = person.name_en
            result.append({
                'href':    reverse('team') + '#%s' % transliterate(name),
                'image':   person.image.url,
                'heading': person.name,
                'content': ' '.join(person.bio.split(' ')[:15]) + '...'
            })

    return HttpResponse(json.dumps(result), mimetype="application/json")


def search(request):
    context = {'page': 'search'}
    return render_to_response('search.html', context, context_instance=RequestContext(request))


def about(request):
    context = {'page': 'about'}
    return render_to_response('about.html', context, context_instance=RequestContext(request))


def contacts(request):
    context = {'page': 'contacts'}
    return render_to_response('contacts.html', context, context_instance=RequestContext(request))


def news(request):
    context = {
        'page': 'news',
        'news': News.objects.all()[:10]
    }
    return render_to_response('news.html', context, context_instance=RequestContext(request))
