from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property
from django.http import JsonResponse

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values('id', 'title', 'description', 'price', 'location', 'created_at')
    return JsonResponse({'data': list(properties)})



    



