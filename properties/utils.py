from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

def get_all_properties():
        properties = cache.get('all_properties')
        if properties is None:
            properties = Property.objects.all()
            cache.set('all_properties', properties, 3600)  # Cache for 1 hour
        return properties

def get_redis_cache_metrics():
        logger = logging.getLogger(__name__)
        try:
            # Connect to Redis using django_redis
            redis_conn = get_redis_connection('default')
            # Get INFO stats
            info = redis_conn.info()
            keyspace_hits = info.get('keyspace_hits', 0)
            keyspace_misses = info.get('keyspace_misses', 0)
            # Calculate hit ratio
            total = keyspace_hits + keyspace_misses
            hit_ratio = (keyspace_hits / total) if total > 0 else 0.0
            # Log metrics
            logger.info(f"Redis Cache Metrics - Hits: {keyspace_hits}, Misses: {keyspace_misses}, Hit Ratio: {hit_ratio:.2%}")
            # Return dictionary
            return {
                'hits': keyspace_hits,
                'misses': keyspace_misses,
                'hit_ratio': hit_ratio
            }
        except Exception as e:
            logger.error(f"Error retrieving Redis metrics: {str(e)}")
            return {'hits': 0, 'misses': 0, 'hit_ratio': 0.0}