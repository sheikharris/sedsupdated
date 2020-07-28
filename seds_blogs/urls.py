from django.urls import path
from . import views
urlpatterns = [
    path('',views.seds_blog,name='blog'),
    path('move/',views.move,name="move"),
    path('movetrending/',views.movetrending,name="movetrending"),
    path('vlog/',views.vlogfun,name="vlog"),
    path('photo/',views.photo,name='astro'),
]
