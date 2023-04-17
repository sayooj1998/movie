from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.models import movie
from . forms import movie_form

# Create your views here.
def index(request):
    m=movie.objects.all()
    condext={
        'movielist':m
    }
    return render(request,'index.html',condext)

def detail(request, movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':m})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()

    return render(request,'add.html')

def update(request,id):
    m=movie.objects.get(id=id)
    form=movie_form(request.POST or None, request.FILES,instance=m)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movie':m})

def delete(request,id):
   if request.method=='POST':
       m=movie.objects.get(id=id)
       m.delete()
       return redirect('/')
   return render(request,'delete.html')