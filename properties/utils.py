from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

def get_all_properties():
    cached_properties = cache.get('all_properties')
    if cached_properties is None:
        queryset = Property.objects.all()
        # Optionally convert queryset to list if serialization is an issue
        cache.set('all_properties', queryset, 3600)  # Cache 1 hour
        return queryset
    return cached_properties

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    redis_client = get_redis_connection("default")
    info = redis_client.info()

    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': hit_ratio,
    }

    logger.info(f"Redis cache metrics: {metrics}")
    return metrics
