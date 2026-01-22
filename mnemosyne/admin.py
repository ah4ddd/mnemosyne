from django.contrib import admin # import Django's built-in admin system
from .models import Entry, Topic # models exist, make it managable

# Expose these tables in the admin UI
admin.site.register(Topic)
admin.site.register(Entry)
