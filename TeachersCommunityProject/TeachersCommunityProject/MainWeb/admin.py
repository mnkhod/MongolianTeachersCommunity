from django.contrib import admin
from django.contrib.admin.sites import AdminSite as site
from .models import Bagsh,News,Law,Comment,ContactUs

class BagshAdmin(admin.ModelAdmin):
    list_display = ('name','email')

# Register your models here.
admin.site.register(Bagsh,BagshAdmin)
admin.site.register(News)
admin.site.register(Law)
admin.site.register(Comment)
admin.site.register(ContactUs)

# Overriding Default Admin Panel Interface Text Contents
site.site_header = "Монголын Багш Нарын Үйлвэрчний Эвлэлийн Холбоо" #Django Administration
site.site_title = "МБНҮЭХ" #Django Site Admin
site.index_title = "Админы Хэсэг" # Site Administration

# AdminSite.index_template
# AdminSite.app_index_template
# AdminSite.login_template
# AdminSite.login_form
# AdminSite.logout_template
# AdminSite.password_change_template
# AdminSite.password_change_done_template
