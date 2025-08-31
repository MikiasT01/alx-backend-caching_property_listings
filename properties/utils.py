from django.core.cache import cache
from .models import Property

def getallproperties():
        properties = cache.get('allproperties')
        if properties is None:
            properties = Property.objects.all()
            cache.set('allproperties', properties, 3600)  # Cache for 1 hour
        return properties