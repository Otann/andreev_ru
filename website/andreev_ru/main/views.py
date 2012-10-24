from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from andreev_ru.main.models import CustomPage, Work

def prepare_base():
	return {
		'pages': CustomPage.objects.all(),
		'works': Work.objects.all(),
	}

def home(request):
	context = prepare_base()
	return render_to_response('home.html', context, context_instance=RequestContext(request))

def works(request):
	context = prepare_base()
	return render_to_response('home.html', context, context_instance=RequestContext(request))

def page(request, slug):
	context = prepare_base()
	context['page'] = get_object_or_404(CustomPage, slug=slug)
	return render_to_response('page.html', context, context_instance=RequestContext(request))

def work(request, slug):
	context = prepare_base()
	context['work'] = get_object_or_404(Work, slug=slug)
	# context['images'] =
	return render_to_response('work.html', context, context_instance=RequestContext(request))
