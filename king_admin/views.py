from django.shortcuts import render
from king_admin import king_showadmin


# Create your views here.


def index(request):
    # print king_showadmin.enabled_admins['crm']['customer']
    list_things =king_showadmin.enabled_admins
    print list_things
    return render(request, 'kind_admin/index.html', {
        'list': list_things,
    })


def index_name(request, app_name, table_name):
    print("-->", app_name, table_name)
    admin_class = king_showadmin.enabled_admins[app_name][table_name]
    print admin_class
    return render(request,'kind_admin/show.html',{
        'admin_class':admin_class,
    })