from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import time, json
from datetime import datetime

def hello(request):
    cookies = dict(request.COOKIES)
    print(cookies)
    resp = JsonResponse(data=cookies)
    resp.set_cookie('test_cookie', 'test_cookie')
    
    expires = datetime.fromtimestamp(time.time()+30*86400)
    resp.set_cookie('test_cookie_expired', 'test_cookie_expired', expires=expires)
    return resp
