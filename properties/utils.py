from django.core.cache import cache
from .models import Property

def get_all_properties():
    cached_properties = cache.get('all_properties')
    if cached_properties is None:
        queryset = Property.objects.all()
        # Optionally convert queryset to list if serialization is an issue
        cache.set('all_properties', queryset, 3600)  # Cache 1 hour
        return queryset
    return cached_properties
