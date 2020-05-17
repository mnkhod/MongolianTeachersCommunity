from django.contrib import admin
from .models import Bagsh,Post,Comment,ContactUs

class BagshAdmin(admin.ModelAdmin):
    list_display = ('name','email')

# Register your models here.
admin.site.register(Bagsh,BagshAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ContactUs)
