# Located in my app that processes orders
from andreev_ru.main.models import CustomPage

def pages_processor(request):
    return {
        'all_pages': CustomPage.objects.exclude(position=0)
    }