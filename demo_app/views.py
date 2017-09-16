from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .script import *
import json
import csv


def calculate_table(mon,tue,wed,thu,fri,cal):
    for c in cal:
        print(c['day'], c['top'], c['height'])

        if c['day'] == 'Mon':    
            if c['top'] == '450': #1
                for e in range(int(c['height'])):
                    mon[e] = 1

            elif c['top'] == '525':
                for e in range(90, 90 + int(c['height'])):
                    print("k")
                    mon[e] = 1

            elif c['top'] == '600':
                for e in range(180, 180 + int(c['height'])):
                    mon[e] = 1

            elif c['top'] == '675':
                for e in range(270, 270 + int(c['height'])):
                    mon[e] = 1                     

            elif c['top'] == '750':
                for e in range(360, 360 + int(c['height'])):
                    mon[e] = 1 

            elif c['top'] == '825':
                for e in range(450, 450 + int(c['height'])):
                    mon[e] = 1 

            elif c['top'] == '900':
                for e in range(540, 540 + int(c['height'])):
                    mon[e] = 1 

            elif c['top'] == '975':
                for e in range(630, 630 + int(c['height'])):
                    mon[e] = 1 

            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    mon[e] = 1


        elif c['day'] == 'Tue':
            if c['top'] == '450': #1
                for e in range(int(c['height'])):
                    tue[e] = 1

            elif c['top'] == '525':
                for e in range(90, 90 + int(c['height'])):
                    tue[e] = 1

            elif c['top'] == '600':
                for e in range(180, 180 + int(c['height'])):
                    tue[e] = 1

            elif c['top'] == '675':
                for e in range(270, 270 + int(c['height'])):
                    tue[e] = 1                     

            elif c['top'] == '750':
                for e in range(360, 360 + int(c['height'])):
                    tue[e] = 1 

            elif c['top'] == '825':
                for e in range(450, 450 + int(c['height'])):
                    tue[e] = 1 

            elif c['top'] == '900':
                for e in range(540, 540 + int(c['height'])):
                    tue[e] = 1 

            elif c['top'] == '975':
                for e in range(630, 630 + int(c['height'])):
                    tue[e] = 1 


            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    tue[e] = 1                   


        elif c['day'] == 'Wed':
            if c['top'] == '450': #1
                for e in range(int(c['height'])):
                    wed[e] = 1

            elif c['top'] == '525':
                for e in range(90, 90 + int(c['height'])):
                    wed[e] = 1

            elif c['top'] == '600':
                for e in range(180, 180 + int(c['height'])):
                    wed[e] = 1

            elif c['top'] == '675':
                for e in range(270, 270 + int(c['height'])):
                    wed[e] = 1                     

            elif c['top'] == '750':
                for e in range(360, 360 + int(c['height'])):
                    wed[e] = 1 

            elif c['top'] == '825':
                for e in range(450, 450 + int(c['height'])):
                    wed[e] = 1 

            elif c['top'] == '900':
                for e in range(540, 540 + int(c['height'])):
                    wed[e] = 1  

            elif c['top'] == '975':
                for e in range(630, 630 + int(c['height'])):
                    wed[e] = 1   

            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    wed[e] = 1


        elif c['day'] == 'Thu':
            if c['top'] == '450': #1
                for e in range(int(c['height'])):
                    thu[e] = 1

            elif c['top'] == '525':
                for e in range(90, 90 + int(c['height'])):
                    thu[e] = 1

            elif c['top'] == '600':
                for e in range(180, 180 + int(c['height'])):
                    thu[e] = 1

            elif c['top'] == '675':
                for e in range(270, 270 + int(c['height'])):
                    thu[e] = 1                     

            elif c['top'] == '750':
                for e in range(360, 360 + int(c['height'])):
                    thu[e] = 1 

            elif c['top'] == '825':
                for e in range(450, 450 + int(c['height'])):
                    thu[e] = 1 

            elif c['top'] == '900':
                for e in range(540, 540 + int(c['height'])):
                    thu[e] = 1 

            elif c['top'] == '975':
                for e in range(630, 630 + int(c['height'])):
                    thu[e] = 1 
            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    thu[e] = 1    

        elif c['day'] == 'Fri':
            if c['top'] == '450': #1
                for e in range(int(c['height'])):
                    fri[e] = 1

            elif c['top'] == '525':
                for e in range(90, 90 + int(c['height'])):
                    fri[e] = 1

            elif c['top'] == '600':
                for e in range(180, 180 + int(c['height'])):
                    fri[e] = 1

            elif c['top'] == '675':
                for e in range(270, 270 + int(c['height'])):
                    fri[e] = 1                     

            elif c['top'] == '750':
                for e in range(360, 360 + int(c['height'])):
                    fri[e] = 1 

            elif c['top'] == '825':
                for e in range(450, 450 + int(c['height'])):
                    fri[e] = 1 

            elif c['top'] == '900':
                for e in range(540, 540 + int(c['height'])):
                    fri[e] = 1 

            elif c['top'] == '975':
                for e in range(630, 630 + int(c['height'])):
                    fri[e] = 1
            elif int(c['top']) < 450:
                for e in range(int(int(c['height'] )-1/ 2)):
                    fri[e] = 1

    result = {"mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri}
    return result

@csrf_exempt
def message(request):
    
    mon = [0] * 660
    tue = [0] * 660
    wed = [0] * 660
    thu = [0] * 660
    fri = [0] * 660
    
    if request.method == "POST":
        
        
        #url = request.GET.get('url', '') 
        #urls = [6212167, 6516752, 6714113, 6967766]
        #urls = [6212167]
        

        urls = request.POST.getlist('table_url')
        print(urls)

        for url in urls:
            driver = webdriver.Chrome()
            everytime_login(driver,"kth5604","fv3528no!",str(url))
            time.sleep(3)

            k = find_class(driver)
            val = calculate_table(mon,tue,wed,thu,fri,k)
            mon = val['mon']
            tue = val['tue']
            wed = val['wed']
            thu = val['thu']
            fri = val['fri']

        result = {"mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri}
        textMessage = {"calculate": result}

    return JsonResponse(textMessage)
