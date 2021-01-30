from django.shortcuts import render
from django.http import HttpResponse
from .forms import LocationForm
from .models import Location 

def home(request):
    form = LocationForm()
    print(Location.objects.all())
    if request.method == 'POST':
        form = LocationForm(request.POST,None)
        if form.is_valid():
            form.save()
        # return HttpResponse(request.POST.items())
    return render(request, "tem.html", {"form":form})  


