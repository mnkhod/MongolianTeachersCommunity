from django.http import HttpResponse
from django.shortcuts import render


#Static
def index(req):
    return HttpResponse("Home")

def about_us(req):
    return HttpResponse("Bidnii Tuhai")

def contact_us(req):
    return HttpResponse("Holboo Barih")

#Dynamic
def news_archive(req):
    return HttpResponse("Medee Archive")

def news_single(req,news_id):
    return HttpResponse("Medee Single")

def laws_archive(req):
    return HttpResponse("Huuli Archive")

def laws_single(req,laws_id):
    return HttpResponse("Huuli Single")
