from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Account

# Create your views here.
@csrf_exempt
def login(request):
    data = {'message':""}
    kakaoID = request.POST.get('kakaoID')

    if not Account.objects.filter(kakaoID=kakaoID).exists():
        account = Account.objects.create(kakaoID=kakaoID)
        data['message'] = "Create"
    else:
        account = Account.objects.get(kakaoID=kakaoID)
        data['message'] = "Login"

    request.session['id'] = account.id
    request.session['kakaoID'] = account.kakaoID

    data["level"] = account.level
    
    return HttpResponse(json.dumps(data), "application/json")
