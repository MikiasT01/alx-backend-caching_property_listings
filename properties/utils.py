from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache for 15 minutes (from Task 1)
def property_list(request):
        properties = get_all_properties().values('id', 'title', 'price', 'location')
        return JsonResponse({
            'data': list(properties)
        })