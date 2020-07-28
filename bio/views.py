from django.shortcuts import render
from django.http import HttpResponse
from .models import bio_info

# Create your views here.
def bio(request):
    bact=bio_info.objects.values("batch").distinct()
    if request.method=='POST':
        bac=request.POST['bac']
        if bac=='all':
           bio=bio_info.objects.all()
           return render(request,'seds_bio.html',{'bio':bio,"drop_bac":bact})
        else:
           bio=bio_info.objects.filter(batch=bac)
           return render(request,'seds_bio.html',{'bio':bio,"drop_bac":bact})


    else:
        bio=bio_info.objects.all()

        return render(request,'seds_bio.html',{'bio':bio,"drop_bac":bact})

def index(request):
    return render(request,'index.html')
