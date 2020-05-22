# Generated by Django 3.0.6 on 2020-05-22 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bagsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Нэр')),
                ('roleDesc', models.CharField(default='', max_length=250, null=True)),
                ('desc', models.TextField(default='', null=True)),
                ('fb', models.URLField(default='', max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Цахим Хаяг')),
                ('profileImg', models.ImageField(upload_to='teachers', verbose_name='Зураг')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Багш',
                'verbose_name_plural': 'Багш Нарын Жагсаалт',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Хэрэглэгчийн Нэр')),
                ('email', models.EmailField(max_length=254, verbose_name='Эмайл Хаяг')),
                ('content', models.TextField(verbose_name='Агуулга')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Сэтгэгдэл',
                'verbose_name_plural': 'Сэтгэгдэлийн Жагсаалт',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=254, verbose_name='Бүтэн Нэр')),
                ('email', models.EmailField(max_length=254, verbose_name='Эмайл Хаяг')),
                ('phone', models.CharField(max_length=12, verbose_name='Утас')),
                ('text', models.TextField(verbose_name='Агуулга')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Бидэнтэй Холбогдох',
                'verbose_name_plural': 'Бидэнтэй Холбогдох Жагсаалт',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='hamtragchBaiguulga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ner', models.CharField(blank=True, default='', max_length=250)),
                ('img', models.ImageField(default='', upload_to='bidniTuhai')),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Мэдээний Төрлийн Нэр')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Мэдээний Төрөл',
                'verbose_name_plural': 'Мэдээний Төрлийн Жагсаалт',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='phoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Сайтын Тохиргоо', editable=False, max_length=250)),
                ('facebook', models.URLField(blank=True, default='')),
                ('twitter', models.URLField(blank=True, default='')),
                ('gmail', models.URLField(blank=True, default='')),
                ('email', models.EmailField(max_length=254)),
                ('googleMap', models.URLField(default='https://www.google.com/maps/embed/v1/place?q=Mongolian%20Development%20Center&key=AIzaSyAdVlR0-lB7cRHnnGhBReo_pUmTEZBAiJs', max_length=900)),
                ('bidniImg', models.ImageField(default='', upload_to='bidniTuhai')),
                ('bidniTitle', models.CharField(blank=True, default='Бидний Тухай', max_length=250)),
                ('bidniMiniDesc', models.CharField(blank=True, default='', max_length=250)),
                ('bidniDesc', models.TextField(blank=True, default='')),
                ('alsinHaraa', models.TextField(blank=True, default='')),
                ('erhemZorilgo', models.TextField(blank=True, default='')),
                ('mendchilgee', models.TextField(blank=True, default='')),
                ('hamtragchBaiguulgaZurga', models.ManyToManyField(to='MainWeb.hamtragchBaiguulga')),
                ('phoneList', models.ManyToManyField(to='MainWeb.phoneNumber')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Гарчиг')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Сайтын Зам')),
                ('newsImg', models.ImageField(upload_to='news', verbose_name='Зураг')),
                ('body', models.TextField(verbose_name='Агуулга')),
                ('featured', models.BooleanField(default=False, null=True, verbose_name='Онцлог Эсэх?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainWeb.Bagsh', verbose_name='Зохиогч')),
                ('categories', models.ManyToManyField(to='MainWeb.NewsCategory', verbose_name='Мэдээний Төрлийн Жагсаалт')),
                ('comments', models.ManyToManyField(blank=True, to='MainWeb.Comment', verbose_name='Холбогдох Сэтгэгдэлийн Жагсаалт')),
            ],
            options={
                'verbose_name': 'Мэдээ',
                'verbose_name_plural': 'Мэдээний Жагсаалт',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Гарчиг')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Сайтын Зам')),
                ('pdf', models.FileField(default=None, upload_to='laws', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Хуулийн PDF Агуулга')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainWeb.Bagsh', verbose_name='Зохиогч')),
            ],
            options={
                'verbose_name': 'Хууль',
                'verbose_name_plural': 'Хуулийн Жагсаалт',
                'ordering': ('-created',),
            },
        ),
    ]
