from django.shortcuts import render
from coaching.models import Coachings

def destinations(request):
    coaching=Coachings.objects.all()
    return render(request,'destinations.html',{'coaching':coaching})
