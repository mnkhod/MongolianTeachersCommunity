from django.http import HttpResponse
from django.shortcuts import render
from .models import News


#Static
def index(req):
    featuredNews = News.objects.filter(featured=True)

    TopTwoNews = News.objects.order_by('created')[:2]


    context = { 'news' : featuredNews , 'topNews' : TopTwoNews }

    return render(req,'index.html',context)

def about_us(req):
    return render(req, 'aboutus.html')

def contact_us(req):
    return render(req,'contactus.html' )

#Dynamic
def news_archive(req):
    return render(req, 'news.html',)

def news_single(req,news_id):
    return render(req,"newscontent.html")

def laws_archive(req):
    return render(req, 'laws.html',)

def laws_single(req,laws_id):
    return render(req, 'lawcontent.html',)
