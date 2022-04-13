from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def fun(request):
    obj=place.objects.all()
    abc=team.objects.all()
    return render (request,'index.html',{'result':obj,'ans':abc})