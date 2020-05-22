from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Bagsh(models.Model):
    name=models.CharField(max_length=250,verbose_name="Нэр")
    roleDesc=models.CharField(max_length=250,default='',null=True)
    desc=models.TextField(default='',null=True)
    fb=models.URLField(max_length=250,default='',null=True)
    email=models.EmailField(null=True,verbose_name="Цахим Хаяг")
    profileImg=models.ImageField(upload_to='teachers',verbose_name="Зураг")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)
        verbose_name="Багш"
        verbose_name_plural="Багш Нарын Жагсаалт"

class NewsCategory(models.Model):
    name=models.CharField(max_length=250,verbose_name="Мэдээний Төрлийн Нэр")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)
        verbose_name="Мэдээний Төрөл"
        verbose_name_plural="Мэдээний Төрлийн Жагсаалт"

class Law(models.Model):
    title=models.CharField(max_length=250,verbose_name="Гарчиг")
    slug=models.SlugField(max_length=250,unique=True,verbose_name="Сайтын Зам")
    author=models.ForeignKey(Bagsh,on_delete=models.CASCADE,verbose_name="Зохиогч")
    pdf=models.FileField(upload_to="laws",verbose_name="Хуулийн PDF Агуулга",
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])], blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-created',)
        verbose_name_plural="Хуулийн Жагсаалт"
        verbose_name="Хууль"


class Comment(models.Model):
    name=models.CharField(max_length=250,verbose_name="Хэрэглэгчийн Нэр")
    email=models.EmailField(verbose_name="Эмайл Хаяг")
    content=models.TextField(verbose_name="Агуулга")
    created=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)
        verbose_name_plural="Сэтгэгдэлийн Жагсаалт"
        verbose_name="Сэтгэгдэл"


class News(models.Model):
    title=models.CharField(max_length=250,verbose_name="Гарчиг")
    slug=models.SlugField(max_length=250,unique=True,verbose_name="Сайтын Зам")
    author=models.ForeignKey(Bagsh,on_delete=models.CASCADE,verbose_name="Зохиогч")
    categories=models.ManyToManyField(NewsCategory,verbose_name="Мэдээний Төрлийн Жагсаалт")
    comments=models.ManyToManyField(Comment,blank=True,verbose_name="Холбогдох Сэтгэгдэлийн Жагсаалт")
    newsImg=models.ImageField(upload_to='news',verbose_name="Зураг")
    body=models.TextField(verbose_name="Агуулга")
    featured=models.BooleanField(default=False,null=True,verbose_name="Онцлог Эсэх?")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-created',)
        verbose_name="Мэдээ"
        verbose_name_plural="Мэдээний Жагсаалт"


class ContactUs(models.Model):
    fullName=models.CharField(max_length=254,verbose_name="Бүтэн Нэр")
    email=models.EmailField(verbose_name="Эмайл Хаяг")
    phone=models.CharField(max_length=12,verbose_name="Утас")
    text=models.TextField(verbose_name="Агуулга")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.fullName

    class Meta:
        ordering =('-created',)
        verbose_name_plural="Бидэнтэй Холбогдох Жагсаалт"
        verbose_name="Бидэнтэй Холбогдох"



# GLOBAL PAGE SETTINGS MODELS

class Settings(models.Model):
    title=models.CharField(max_length=250,default='Сайтын Тохиргоо',editable=False)

    # Social Media
    facebook=models.URLField(max_length=200,default='',blank=True);
    twitter=models.URLField(max_length=200,default='',blank=True);
    gmail=models.URLField(max_length=200,default='',blank=True);

    # Holboo Barih
    phoneList=models.ManyToManyField('phoneNumber')
    email=models.EmailField(max_length=254)

    googleMap=models.URLField(
            max_length=900,default="https://www.google.com/maps/embed/v1/place?q=Mongolian%20Development%20Center&key=AIzaSyAdVlR0-lB7cRHnnGhBReo_pUmTEZBAiJs")


    # Bidni Tuhai
    bidniImg=models.ImageField(upload_to='bidniTuhai',default='')
    bidniTitle=models.CharField(max_length=250,default='Бидний Тухай',blank=True)
    bidniMiniDesc=models.CharField(max_length=250,default='',blank=True)
    bidniDesc=models.TextField(default='',blank=True)
    hamtragchBaiguulgaZurga=models.ManyToManyField('hamtragchBaiguulga')

    alsinHaraa=models.TextField(default='',blank=True)
    erhemZorilgo=models.TextField(default='',blank=True)
    mendchilgee=models.TextField(default='',blank=True)

    def __str__(self):
        return self.title

class phoneNumber(models.Model):
    phone=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.phone

class hamtragchBaiguulga(models.Model):
    ner=models.CharField(max_length=250,default='',blank=True)
    img=models.ImageField(upload_to='bidniTuhai',default='')

    def __str__(self):
        return self.ner
