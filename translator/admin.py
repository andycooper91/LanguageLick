from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Language)
admin.site.register(PhraseSource)
admin.site.register(Phrase)
admin.site.register(Translation)