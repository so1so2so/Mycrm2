from django.shortcuts import render, HttpResponse


# Create your views here.
def index(requset):
    return render(requset, 'index.html')
    # return HttpResponse('zhangneb')
