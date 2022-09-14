from django.shortcuts import render
from .models import Post,Mainpost

# Create your views here.
def civomian(request):
    data = Post.objects.all()
    datamain = Mainpost.objects.all()
    return render(request,'news/civomian.html',{'data':data,'datam':datamain})