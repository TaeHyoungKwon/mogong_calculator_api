from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .script import *
import json
import csv
import time

'''
def calculate_table(mon,tue,wed,thu,fri,cal):
    for c in cal:
        print(c['day'], c['top'], c['height'])

        if c['day'] == 'Mon':    
            if c['top'] == '540': #1
                for e in range(int(c['height'])-1):
                    mon[e] = 1

            elif c['top'] == '630':
                for e in range(90, 90 + int(c['height'])-1):
                    print("k")
                    mon[e] = 1

            elif c['top'] == '720':
                for e in range(180, 180 + int(c['height'])-1):
                    mon[e] = 1

            elif c['top'] == '810':
                for e in range(270, 270 + int(c['height'])-1):
                    mon[e] = 1                     

            elif c['top'] == '1080':
                for e in range(360, 360 + int(c['height'])-1):
                    mon[e] = 1 

            elif c['top'] == '990':
                for e in range(450, 450 + int(c['height'])-1):
                    mon[e] = 1 

            elif c['top'] == '1080':
                for e in range(540, 540 + int(c['height'])-1):
                    mon[e] = 1 

            elif c['top'] == '1130':
                for e in range(630, 630 + int(c['height'])-1):
                    mon[e] = 1 

            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    mon[e] = 1


        elif c['day'] == 'Tue':
            if c['top'] == '540': #1
                for e in range(int(c['height'])-1):
                    tue[e] = 1

            elif c['top'] == '630':
                for e in range(90, 90 + int(c['height'])-1):
                    tue[e] = 1

            elif c['top'] == '720':
                for e in range(180, 180 + int(c['height'])-1):
                    tue[e] = 1

            elif c['top'] == '810':
                for e in range(270, 270 + int(c['height'])-1):
                    tue[e] = 1                     

            elif c['top'] == '1080':
                for e in range(360, 360 + int(c['height'])-1):
                    tue[e] = 1 

            elif c['top'] == '990':
                for e in range(450, 450 + int(c['height'])-1):
                    tue[e] = 1 

            elif c['top'] == '1080':
                for e in range(540, 540 + int(c['height'])-1):
                    tue[e] = 1 

            elif c['top'] == '1130':
                for e in range(630, 630 + int(c['height'])-1):
                    tue[e] = 1 


            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    tue[e] = 1                   


        elif c['day'] == 'Wed':
            if c['top'] == '540': #1
                for e in range(int(c['height'])-1):
                    wed[e] = 1

            elif c['top'] == '630':
                for e in range(90, 90 + int(c['height'])-1):
                    wed[e] = 1

            elif c['top'] == '720':
                for e in range(180, 180 + int(c['height'])-1):
                    wed[e] = 1

            elif c['top'] == '810':
                for e in range(270, 270 + int(c['height'])-1):
                    wed[e] = 1                     

            elif c['top'] == '1080':
                for e in range(360, 360 + int(c['height'])-1):
                    wed[e] = 1 

            elif c['top'] == '990':
                for e in range(450, 450 + int(c['height'])-1):
                    wed[e] = 1 

            elif c['top'] == '1080':
                for e in range(540, 540 + int(c['height'])-1):
                    wed[e] = 1  

            elif c['top'] == '1130':
                for e in range(630, 630 + int(c['height'])-1):
                    wed[e] = 1   

            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    wed[e] = 1


        elif c['day'] == 'Thu':
            if c['top'] == '540': #1
                for e in range(int(c['height'])-1):
                    thu[e] = 1

            elif c['top'] == '630':
                for e in range(90, 90 + int(c['height'])-1):
                    thu[e] = 1

            elif c['top'] == '720':
                for e in range(180, 180 + int(c['height'])-1):
                    thu[e] = 1

            elif c['top'] == '810':
                for e in range(270, 270 + int(c['height'])-1):
                    thu[e] = 1                     

            elif c['top'] == '1080':
                for e in range(360, 360 + int(c['height'])-1):
                    thu[e] = 1 

            elif c['top'] == '990':
                for e in range(450, 450 + int(c['height'])-1):
                    thu[e] = 1 

            elif c['top'] == '1080':
                for e in range(540, 540 + int(c['height'])-1):
                    thu[e] = 1 

            elif c['top'] == '1130':
                for e in range(630, 630 + int(c['height'])-1):
                    thu[e] = 1 
            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    thu[e] = 1    

        elif c['day'] == 'Fri':
            if c['top'] == '540': #1
                for e in range(int(c['height'])-1):
                    fri[e] = 1

            elif c['top'] == '630':
                for e in range(90, 90 + int(c['height'])-1):
                    fri[e] = 1

            elif c['top'] == '720':
                for e in range(180, 180 + int(c['height'])-1):
                    fri[e] = 1

            elif c['top'] == '810':
                for e in range(270, 270 + int(c['height'])-1):
                    fri[e] = 1                     

            elif c['top'] == '1080':
                for e in range(360, 360 + int(c['height'])-1):
                    fri[e] = 1 

            elif c['top'] == '990':
                for e in range(450, 450 + int(c['height'])-1):
                    fri[e] = 1 

            elif c['top'] == '1080':
                for e in range(540, 540 + int(c['height'])-1):
                    fri[e] = 1 

            elif c['top'] == '1130':
                for e in range(630, 630 + int(c['height'])-1):
                    fri[e] = 1


    result = {"mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri}
    return result
'''


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
        
        
        #url = request.GET.get('url', '') 
        #urls = [6212167, 6516752, 6714113, 6967766]
        #urls = [6212167]
        
        urls = []
        #urls = request.POST.getlist('table_url[]')
        url_dict = request.POST.dict()

        for url in url_dict:
            urls.append(url_dict[url])

        print(request.POST)
        print(urls)
        

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
        textMessage = {"calculate": result}
        end = time.time() - start
        print(end)

    return JsonResponse(textMessage)



