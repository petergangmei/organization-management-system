from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from event_app.models import NewsModel

def news(request):
    news    = NewsModel.objects.filter(public=True)
    context ={
        'news':news,
    }
    return render(request,'news.html',context)

def news_detail(request,slug):
    try:
        news = NewsModel.objects.get(slug=slug)
    except NewsModel.DoesNotExist:
        messages.error(request,"Article now found!")
        return redirect(reverse("event_app:news"))


    context ={
        'news':news,
    }
    return render(request,'news-detail.html',context)