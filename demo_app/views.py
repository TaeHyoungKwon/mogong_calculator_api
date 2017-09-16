from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .script import *
import json
import csv
import time


def calculate_table(mon,tue,wed,thu,fri,cal):
    
    val = 540

    for c in cal:
        print(c['day'], c['top'], c['height'])

        default_val = int(c['top']) - val

        if default_val < 0:
            default_val = 0
            

        if c['day'] == 'Mon':
            for e in range(default_val, int(c['top']) - val +  int(c['height'])-1):
                mon[e] = 1
                

        elif c['day'] == 'Tue':
            for e in range(default_val,int(c['top']) - val + int(c['height'])-1):
                tue[e] = 1
                
        elif c['day'] == 'Wed':
            for e in range(default_val,int(c['top']) - val + int(c['height'])-1):
                wed[e] = 1
                

        elif c['day'] == 'Thu':
            for e in range(default_val,int(c['top']) - val + int(c['height'])-1):
                thu[e] = 1
                

        elif c['day'] == 'Fri':
            for e in range(default_val,int(c['top']) - val + int(c['height'])-1):
                fri[e] = 1
                
    
    result = {"mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri}
    return result

@csrf_exempt
def message(request):
    
    start = time.time()
    
    mon = [0] * 660
    tue = [0] * 660
    wed = [0] * 660
    thu = [0] * 660
    fri = [0] * 660
    
    if request.method == "POST":
        """
        urls = []
        urls = request.POST.getlist('table_url')
        """
        
        urls = []
        
        url_dict = request.POST.dict()

        for url in url_dict:
            urls.append(url_dict[url])      
        

        for url in urls:
            driver = webdriver.PhantomJS()
            
            everytime_login(driver,"kth5604","fv3528no!",url)
            time.sleep(1)
            
            k = find_class(driver)

            val = calculate_table(mon,tue,wed,thu,fri,k)
            mon = val['mon']
            tue = val['tue']
            wed = val['wed']
            thu = val['thu']
            fri = val['fri']

        result = {"mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri}

        result1 = {'0' : calc_start_end(mon), '1' : calc_start_end(tue), '2' : calc_start_end(wed), '3' : calc_start_end(thu), '4' : calc_start_end(fri)}
        textMessage = {"calculate": result1}
        end = time.time() - start

    return JsonResponse(textMessage)



def calc_start_end(week):
    
    start_init = False
    result = []
    for idx in range(len(week)):
        if week[idx] == 0 and start_init == False:
            start = idx
            start_init = True
        elif week[idx] == 0:
            if idx == len(week) -1:
                end = idx
                val = {'start':start, 'end':end, 'gap':end - start + 1}
                result.append(val)
            else:
                pass

        elif week[idx] == 1 and start_init == True:
            end = idx-1
            start_init = False
            val = {'start':start, 'end':end, 'gap':end - start + 1}
            result.append(val)

    return result
    

    
        
            
            
        
            
        
        
    



