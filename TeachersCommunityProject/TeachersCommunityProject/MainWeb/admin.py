from django.contrib import admin
from .models import Bagsh,News,Law,Comment,ContactUs

class BagshAdmin(admin.ModelAdmin):
    list_display = ('name','email')

# Register your models here.
admin.site.register(Bagsh,BagshAdmin)
admin.site.register(News)
admin.site.register(Law)
admin.site.register(Comment)
admin.site.register(ContactUs)
