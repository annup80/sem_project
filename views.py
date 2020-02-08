from django.shortcuts import render
from django.http import HttpResponse
from Blood_Management_System.models import campaign
from Blood_Management_System.models import donater

import csv
# Create your views here.

def index(request):
    return render( request , 'index.html')


def profile(request):
    return render (request,'profile.html')


def getfile(request):
    if request.method=='POST':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"' 
        bms=campaign.objects.all()
        writer=csv.writer(response)
        for bm in bms:
            writer.writerow([bm.camp_name,bm.venue,bm.time,bm.img,bm.desc])
        return response
    else:
        return render (request,'csv.html')



def barchart(request):
    c=0
    d=0
    e=0
    f=0
    queryset = donater.objects.all()
    for qset in queryset:
        asa=qset.blood_grp
        if asa=='O+ve':
            c=c+1    
        elif asa=='O-ve':
            d=d+1
        elif asa=='B+ve':
            e=e+1
        else:
            f=f+1
    return render(request, 'csv.html', {'setss':[c,d,e,f]})
    
       
