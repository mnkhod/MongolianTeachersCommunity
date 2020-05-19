from django.http import HttpResponse
from django.shortcuts import render
from .models import News, NewsCategory, ContactUs, Law, Comment , Bagsh


#Static
def index(req):
    featuredNews = News.objects.filter(featured=True)

    topTwoNews = News.objects.order_by('created')[:2]
    latestNews = News.objects.order_by('updated')[:3]


    context = { 'news' : featuredNews , 'topNews' : topTwoNews, 'latestNews' : latestNews }
  
    return render(req,'index.html',context)

def about_us(req):
    return render(req, 'aboutus.html')

def contact_us(req):
    if req.method == 'POST':
        item = ContactUs(fullName=req.POST['fname'],email=req.POST['email']
            ,phone=req.POST['phone'],text=req.POST['content'])
        item.save()
    
    return render(req,'contactus.html' )

#Dynamic
def news_archive(req):
    featuredNews = News.objects.filter(featured=True)
    latestNews = News.objects.order_by('updated')[:3]
    news = News.objects.all()
    allCategories = NewsCategory.objects.all()

    context = { 'featuredNews' : featuredNews , 'news' : news, 'latestNews' : latestNews , 'categories' : allCategories }

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
    laws = Law.objects.all()

    context = { 'laws' : laws}

    return render(req, 'laws.html',context)

def laws_single(req,laws_slug):
    laws = Law.objects.get(slug=laws_slug)

    context = {'laws' : laws }
    return render(req, 'lawcontent.html',context)
