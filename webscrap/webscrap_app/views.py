from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from . models import Link


# Create your views here.
def home(request):

    if request.method == 'POST': 
        newlink = request.POST.get('page', '')
        urls = requests.get(newlink) 
        beautifuldoup = BeautifulSoup(urls.text, 'html.parser')

        for link in beautifuldoup.find_all('a'):
            linkaddress = link.get('href')
            linkname = link.string
            Link.objects.create(address= linkaddress, stringname= linkname)
        
        return HttpResponseRedirect('/')
    
    else:
        # address.append((link.get('href'))) 
        data_value = Link.objects.all()
    return render(request, 'home.html',{'data_value':data_value})

def clear(request):
    Link.objects.all().delete()
    

    return redirect('/')