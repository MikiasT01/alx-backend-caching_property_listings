from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
        properties = Property.objects.all().values('id', 'title', 'price', 'location')
        return JsonResponse({
            'data': list(properties)
        })