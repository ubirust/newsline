from django.contrib import admin
from .models import Note, Advertisement, Achievement, Event

# Register your models here.
admin.site.register(Note)
admin.site.register(Advertisement)
admin.site.register(Achievement)
admin.site.register(Event)
