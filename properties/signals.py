from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Property

@receiver(post_save, sender=Property)
def invalidate_property_cache_save(sender, instance, **kwargs):
        cache.delete('all_properties')
@receiver(post_delete, sender=Property)
def invalidate_property_cache_delete(sender, instance, **kwargs):
        cache.delete('all_properties')