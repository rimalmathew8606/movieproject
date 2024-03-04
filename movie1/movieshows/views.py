from django.db.models import Q
from django.shortcuts import render,redirect
from movieshows.models import movieshows
from django.http import HttpResponse
from movieshows.forms import movieform




# Create your views here.
def home(request):
    v = movieshows.objects.all()
    return render(request, 'home.html',{'mov':v})


def details(request,movie_id):
    movie=movieshows.objects.get(id=movie_id)
    return render(request,'detail.html',{'mov':movie})


def addmovies(request):
    if request.method == 'POST':
        name = request.POST.get('m')
        description = request.POST.get('a')
        year = request.POST.get('p')
        image = request.FILES.get('k')

        # Create a new Movie instance and save it to the database
        mov = movieshows(name=name, description=description, year=year, image=image)
        mov.save()
        return redirect('movieshows:viewmovie')       # Redirect or return a success response

    return render(request, 'addmovies.html')
def viewmovie(request):
    k = movieshows.objects.all()
    return render(request, 'viewmovie.html', context={'mov': k})
def edit(request,p):
    mov=movieshows.objects.get(id=p)
    if (request.method == "POST"):
        form = movieform(request.POST,request.FILES,instance=mov)
        if form.is_valid():
            form.save()
            return viewmovie(request)
    form=movieform(instance=mov)

    return render(request,'edit.html',{'form':form})

def delete(request,p):
    mov = movieshows.objects.get(id=p)
    mov.delete()
    return viewmovie(request)


