from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def app2_str(request):
    return HttpResponse('JAI SURYA BHAI')

def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')