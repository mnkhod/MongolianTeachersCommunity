from django.contrib import admin
from django.contrib.admin.sites import AdminSite as site
from .models import Bagsh,News,Law,Comment,ContactUs,NewsCategory
from .models import Settings,phoneNumber,hamtragchBaiguulga

class BagshAdmin(admin.ModelAdmin):
    list_display = ('name','email')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','featured')
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('title','featured')
    search_fields = ['title']

class LawsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

# Register your models here.
admin.site.register(Bagsh,BagshAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Law,LawsAdmin)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(NewsCategory)



class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Олон Нийтийн Сүлжээ',{ 'fields': ('facebook','twitter','gmail') }),
        ('Бидэндээ Холбоо Барих',{ 'fields': ('phoneList','email','googleMap') }),
        ('Бидний Тухай',{ 'fields': ('bidniTitle','bidniMiniDesc','bidniDesc'
                ,'bidniImg','hamtragchBaiguulgaZurga','alsinHaraa','erhemZorilgo'
                                ,'mendchilgee' ) }),
    )
    list_display = ('title','email','facebook','twitter','gmail')

    def has_add_permission(self,req):
        size = Settings.objects.all()

        if(len(size) ==  0):
            new_item = Settings()
            new_item.save()

        return False

    def has_delete_permission(self,req,obj=None):
        return False

# HIDED THIS MODEL BUT IT IS STILL REGISTERED! HENCE U CAN ADD
class PhoneNumberAdmin(admin.ModelAdmin):
    def get_model_perms(self,req):
        return {}

class HamtragchBaiguulgaAdmin(admin.ModelAdmin):
    def get_model_perms(self,req):
        return {}

admin.site.register(Settings,SettingsAdmin)
admin.site.register(phoneNumber,PhoneNumberAdmin)
admin.site.register(hamtragchBaiguulga,HamtragchBaiguulgaAdmin)

# Overriding Default Admin Panel Interface Text Contents
site.site_header = "Монголын Багш Нарын Үйлдвэрчний Эвлэлийн Холбоо" #Django Administration
site.site_title = "МБНҮЭХ" #Django Site Admin
site.index_title = "Админы Хэсэг" # Site Administration

# AdminSite.index_template
# AdminSite.app_index_template
# AdminSite.login_template
# AdminSite.login_form
# AdminSite.logout_template
# AdminSite.password_change_template
# AdminSite.password_change_done_template
