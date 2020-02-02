from django.shortcuts import render
from django.http import HttpResponse
from Blood_Management_System.models import campaign
import csv
# Create your views here.

def index(request):
    return render( request , 'index.html')


def profile(request):
    return render (request,'profile.html')


def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"' 
    bms=campaign.objects.all()
    writer=csv.writer(response)
    for bm in bms:
        writer.writerow([bm.camp_name,bm.venue,bm.time,bm.img,bm.desc])
    return response
    