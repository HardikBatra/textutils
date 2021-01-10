# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'hardik'}
    return render(request,'index.html',params)
def analyze(request):
    text= request.GET.get('text','default')
    name=request.GET.get('cap','off')
    LOW=request.GET.get('low','off')
    if name=='on':
        text=text.upper()
        params={'atext':text}
    elif LOW=='on':
        text=text.lower()
        params={'atext':text}
    else:
        return "error"
    return render(request,'analyze.html',params)
        
    
    # return HttpResponse("hello")