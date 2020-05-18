from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Bagsh(models.Model):
    name=models.CharField(max_length=250,verbose_name="Нэр")
    email=models.EmailField(verbose_name="Цахим Хаяг")
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

class News(models.Model):
    title=models.CharField(max_length=250,verbose_name="Гарчиг")
    slug=models.SlugField(max_length=250,unique=True,verbose_name="Сайтын Зам")
    author=models.ForeignKey(Bagsh,on_delete=models.CASCADE,verbose_name="Зохиогч")
    categories=models.ManyToManyField(NewsCategory,verbose_name="Мэдээний Төрлийн Жагсаалт",related_name="turuls")
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
    news_id=models.ForeignKey(News,on_delete=models.CASCADE,verbose_name="Холбогдох Мэдээ")

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)
        verbose_name_plural="Сэтгэгдэлийн Жагсаалт"
        verbose_name="Сэтгэгдэл"


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
