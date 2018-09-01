from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseBase
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json

from .models import Account


# Create your views here.
@csrf_exempt
def login(request):
    data = {'message': ""}
    kakaoID = request.POST.get('kakaoID')

    if not Account.objects.filter(kakaoID=kakaoID).exists():
        account = Account.objects.create(kakaoID=kakaoID)
        data['message'] = "Create"
    else:
        account = Account.objects.get(kakaoID=kakaoID)
        data['message'] = "Login"

    request.session['id'] = account.id
    request.session['kakaoID'] = account.kakaoID

    data['account'] = model_to_dict(account)

    return HttpResponse(json.dumps(data), "application/json")


@csrf_exempt
def feed_seolgi(request):
    data = {'message': ""}

    userSeq = request.POST.get("id")
    account = Account.objects.get(id=userSeq)
    exp = request.POST.get('exp')
    account.feed(exp)
    account.save()

    data['account'] = model_to_dict(account)
    
    return HttpResponse(json.dumps(data), "application/json")
