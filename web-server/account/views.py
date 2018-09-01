from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Account

# Create your views here.
def login(request):
    data = {'message':""}
    kakaoID = request.POST.get('kakaoid')

    if not Account.objects.filter(kakaoID=kakaoID).exists():
        account = Account.objects.create(kakaoID=kakaoID)
        data['message'] = "Create"
    else:
        account = Account.objects.get(kakaoID=kakaoID)
        data['message'] = "Login"

    data["level"] = account.level
    
    return HttpResponse(json.dumps(data), "application/json")
