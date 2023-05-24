from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_str(request):
    return HttpResponse('JAI BALAYYA')
def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')