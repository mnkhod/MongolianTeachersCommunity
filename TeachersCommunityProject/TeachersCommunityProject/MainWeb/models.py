from django.db import models
from django.utils import timezone
# Create your models here.

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
        verbose_name_plural="Багш Нар"

class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    author=models.ForeignKey(Bagsh,on_delete=models.CASCADE)
    body=models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)

class Comment(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True,editable=False)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)

class ContactUs(models.Model):
    fullName=models.CharField(max_length=254)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    text=models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.fullName

    class Meta:
        ordering =('-created',)
