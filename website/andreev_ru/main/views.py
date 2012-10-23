from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from andreev_ru.main.models import *

def home(request):
	all_pages = CustomPage.objects.all()
	return render_to_response('home.html', 
		{
			'pages': all_pages 
		},
		context_instance=RequestContext(request)
	)

def page(request, page_id):
	page = get_object_or_404(CustomPage, pk=page_id)
	return render_to_response('page.html', 
		{
			'page': page 
		},
		context_instance=RequestContext(request)
	)

def work_detail(request, work_id):
	work = get_object_or_404(Work, pk=work_id)
	return HttpResponse("You're looking at work %s." % work_id)

	return render_to_response('work.html', 
		{
			'pages': all_pages 
		},
		context_instance=RequestContext(request)
	)
