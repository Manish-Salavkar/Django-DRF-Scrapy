# JobHub\accounts\management\commands\showcache.py
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.core.cache.backends.locmem import LocMemCache
import json

class Command(BaseCommand):
    help = 'Displays the contents of the default cache'

    def handle(self, *args, **kwargs):
        cache_data = {}
        if isinstance(cache, LocMemCache):
            for key in cache._cache.keys():
                cache_data[key.decode()] = cache.get(key).decode()
            formatted_cache_data = json.dumps(cache_data, indent=4)
            self.stdout.write(formatted_cache_data)
        else:
            self.stdout.write(self.style.WARNING('Default cache is not using LocMemCache.'))

class Command(BaseCommand):
    help = 'Clears the default cache'

    def handle(self, *args, **kwargs):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Default cache cleared successfully'))