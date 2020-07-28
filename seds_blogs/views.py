from django.shortcuts import render,redirect
from .models import blog,categories,Trending_blog,vlog,video_categories,vlog_trending,Astrophotography_trending,Astrophotography,categories_Astrophotography
# Create your views here.

from django.http import HttpResponse
def seds_blog(request):

    if request.method=='POST':
        fil=request.POST['cat']
        cate=categories.objects.all()
        Trending=Trending_blog.objects.all()
        if fil=='All' or fil=='Categories' :
            blogs=blog.objects.values("title",'blog_link','img_link','summary').distinct()
            fil=''
        else:
          blogs=blog.objects.filter(categories_id=fil).all()
          fil=categories.objects.get(id=fil)
        dist={
         "blogs":blogs,
          "cate":cate,
          "Trending":Trending,
          'categories':fil,

        }
        return render(request,"seds_blog.html",dist)


    else :
        blogs=blog.objects.values("title",'blog_link','img_link','summary').distinct()
        cate=categories.objects.all()
        Trending=Trending_blog.objects.all()
        dist={
          "blogs":blogs,
          "cate":cate,
          "Trending":Trending,

        }
        return render(request,"seds_blog.html",dist)

def move(request):
    link=request.POST['button']
    return redirect(link)


def movetrending(request):
    link=request.POST['Trending_button']
    return redirect(link)


def vlogfun(request):
    tvid=vlog_trending.objects.all()
    vcate=video_categories.objects.all()
    if request.method=='POST':
        cat=request.POST['search_op']
        
        if cat=='All' or cat=='Categories':
            videos=vlog.objects.values('title','summary','link_video','video_categories').distinct()
        else:

            videos=vlog.objects.filter(video_categories=cat).all()

        dist={
            "videos":videos,
            "vcate":vcate,
            "tvid":tvid,

            }
        #return HttpResponse("hi")
        return render(request,'vlog.html',dist)
    else:
        videos=vlog.objects.values('title','summary','link_video','video_categories').distinct()
        dist={
        "videos":videos,
        "vcate":vcate,
        "tvid":tvid,

        }
        return render(request,'vlog.html',dist)

def photo(request):
    Trending_photos=Astrophotography_trending.objects.all()
    photos=Astrophotography.objects.values('title','summary','Astrophotography_link','date','categories').distinct()
    cate=categories_Astrophotography.objects.all()
    if request.method=='POST':
        cat=request.POST['cat']
        photos=Astrophotography.objects.filter(categories=cat).all()



    dist={
    "Trending_photos":Trending_photos,
    "photos":photos,
    'cate':cate,

    }
    return render(request,'grand.html',dist)
