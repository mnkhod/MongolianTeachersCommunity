from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import News, NewsCategory, ContactUs, Law, Comment , Bagsh
from .models import Settings


#Static
def index(req):
    featuredNews = News.objects.filter(featured=True)

    topTwoNews = News.objects.order_by('created')[:2]
    latestNews = News.objects.order_by('updated')[:3]


    context = { 'news' : featuredNews , 'topNews' : topTwoNews, 'latestNews' : latestNews }

    return render(req,'index.html',context)

def about_us(req):
    setting = Settings.objects.all()[0]
    teachers = Bagsh.objects.all()

    context = { 'setting' : setting, 'teachers' : teachers }

    return render(req, 'aboutus.html',context)

def contact_us(req):
    setting = Settings.objects.all()[0]

    context = { 'setting' : setting }

    if req.method == 'POST':
        item = ContactUs(fullName=req.POST['fname'],email=req.POST['email']
            ,phone=req.POST['phone'],text=req.POST['content'])
        item.save()

    return render(req,'contactus.html',context )

#Dynamic
def news_archive(req):
    featuredNews = News.objects.filter(featured=True)
    latestNews = News.objects.order_by('updated')[:3]
    allCategories = NewsCategory.objects.all()

    # Paginator
    objectList = News.objects.all()

    paginator = Paginator(objectList,5)
    page = req.GET.get('page')
    page_size = paginator.num_pages
    page_arr = range(1,page_size+1)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = { 'featuredNews' : featuredNews
               , 'news' : news
               , 'latestNews' : latestNews
               , 'categories' : allCategories
               , 'pageArray' : page_arr
               , 'page' : page}

    if req.method == 'POST':
        item = ContactUs(fullName=req.POST['fname'],email=req.POST['email']
            ,phone=req.POST['phone'],text=req.POST['content'])
        item.save()

    return render(req, 'news.html',context)

def news_single(req,news_slug):
    featuredNews = News.objects.filter(featured=True)
    latestNews = News.objects.order_by('updated')[:3]
    news = News.objects.get(slug=news_slug)
    isBagsh = False

    if req.method == 'POST':
        item = Comment(name=req.POST['name'],email=req.POST['email']
            ,content=req.POST['content'])
        item.save()
        news.comments.add(item)
        news.save()

    context = {'featuredNews' : featuredNews , 'news' : news, 'latestNews' : latestNews , 'isBagsh' : isBagsh}
    return render(req,"newscontent.html",context)

def laws_archive(req):
    # Paginator
    objectList = Law.objects.all()

    paginator = Paginator(objectList,6)
    page = req.GET.get('page')
    page_size = paginator.num_pages
    page_arr = range(1,page_size+1)

    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)

    context = { 'laws' : laws
                ,'page' : page
                , 'pageArray' : page_arr
               }

    return render(req, 'laws.html',context)

def laws_single(req,laws_slug):
    laws = Law.objects.get(slug=laws_slug)
    all_laws = Law.objects.all()

    context = {'laws' : laws , 'all' : all_laws}
    return render(req, 'lawcontent.html',context)
