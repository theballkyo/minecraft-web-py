from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from mcstatus import MinecraftServer
from user.models import Account, Fe

def index(request):
    try:
        server = MinecraftServer.lookup(settings.MC_HOST)
        status = server.status()
        query = server.query()
    except:
        status = None
        query = None
    user = Account.objects.all()
    # print(user.get(username='theballkyo').password)
    top_m = Fe.objects.exclude(name__contains='-').order_by('name')
    return render(request, 'portal/index.html', {'status': status, 'query': query, 'top_m': top_m, 'user': user})

def maps(request):
    return render(request, 'portal/maps.html')
