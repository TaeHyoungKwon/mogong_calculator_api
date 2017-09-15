from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .script import *


@csrf_exempt
def message(request):
    
    if request.method == "GET":
        
        driver = webdriver.Firefox()

        url = request.GET.get('url', '')
        print(url)
        
        everytime_login(driver,"kth5604","fv3528no!",url)
        time.sleep(2)
        
        textMessage = {"calculate": find_class(driver)}

    return JsonResponse(textMessage)
