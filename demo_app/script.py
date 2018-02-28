from selenium import webdriver
import time
import datetime

def everytime_login(driver, User_id, User_pw, url, cnt):

    if cnt == 0:
        driver.get(url)

        #driver.get("http://everytime.kr/timetable/2017/2/6212167")
        driver.find_element_by_css_selector("form")
        elem = driver.find_element_by_name("userid")
        elem.send_keys(User_id)
        elem = driver.find_element_by_name("password")
        elem.send_keys(User_pw)
        elem.submit()
    else:
        driver.get(url)

        return driver


def calculate_time(top, height, i, cnt):
    
    if top == '450':
        start_time = datetime.timedelta(hours=9, minutes = 0)
    elif top == '525':
        start_time = datetime.timedelta(hours=10, minutes = 30)
    elif top == '600':
        start_time = datetime.timedelta(hours=12, minutes = 0)  
    elif top == '675':
        start_time = datetime.timedelta(hours=13, minutes = 30)
    elif top == '750':
        start_time = datetime.timedelta(hours=15, minutes = 0)
    elif top == '825':
        start_time = datetime.timedelta(hours=16, minutes = 30)
    elif top == '900':
        start_time = datetime.timedelta(hours=18, minutes = 0)        
        
    #class_time = datetime.timedelta(minutes=(int(height)-1))
    #end_time = start_time + class_time + datetime.timedelta(minutes = int(15 * ((int(height)-1) / 75 -1)))

    if i == 1:
        week = 'Mon'
    elif i == 2:
        week = 'Tue'
    elif i == 3:
        week = 'Wed'
    elif i == 4:
        week = 'Thu'
    elif i == 5:
        week = 'Fri'

    k = {'index' : cnt, 'day' : week, 'top' : top,'height' : height}

    #print(k['top'] + "/" + k['height'])

    return k


def find_class(driver):
    
    driver.set_window_size(1920, 1080)

    elem = driver.find_element_by_class_name("tablebody")
    day_elem = elem.find_elements_by_tag_name('td')
    i = 0
    cnt =0

    calculate = []
    
    for day in day_elem:
        i +=1
        
        for sub in day.find_elements_by_css_selector('div.cols div.subject'):
            style = sub.get_attribute('style').split(' ')

            height = style[1].replace('px;', "")
            top = style[3].replace('px;', "")
            
            if  i == 1:
                calculate.append(calculate_time(top, height, i, cnt))
            elif i == 2:
                calculate.append(calculate_time(top, height, i, cnt))
            elif i == 3:
                calculate.append(calculate_time(top, height, i, cnt))
            elif i == 4:
                calculate.append(calculate_time(top, height, i, cnt))
            elif i == 5:
                calculate.append(calculate_time(top, height, i, cnt))
            cnt += 1
                
    return calculate              
                    

if __name__ == "__main__":
    
    driver = webdriver.Firefox()
        
    everytime_login(driver,ID,PW)
    time.sleep(1)
    
    print(find_class(driver))
    time.sleep(1)
    driver.close()
   
