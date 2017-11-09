from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print request.user.userprofile.roles.all
    return render(request, 'base_index.html')
    # return HttpResponse('zhangneb')


def sale_index(request):
    return render(request, 'sale/index.html')


def sole_baobiao(request):
    return render(request, 'sale/baob.html')
