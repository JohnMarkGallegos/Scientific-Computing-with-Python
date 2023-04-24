# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:27:56 2023

@author: johnm
"""

def add_time(start_time,duration,param="") :
    param = param.lower()
    weekday = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    
    start_hour = int(start_time.split(':')[0].strip())
    start_min = start_time.split(':')[1].strip()
    duration_hour = int(duration.split(':')[0].strip())*60
    duration_min = int(duration.split(':')[1].strip())
    if "AM" in start_min :
        start_min = start_min.split('A')[0].strip()
        if start_hour == 12 :
            start_hour = 0
        else :
            start_hour = start_hour*60
    if "PM" in start_min :
        start_min = start_min.split('P')[0].strip()
        if start_hour == 12 :
            start_hour = 720
        else :
            start_hour = start_hour*60 + 720   
    start_min = int(start_min)
    value = start_hour + start_min + duration_hour + duration_min
    result_mintues = value%1440
    whole_day = int((value - result_mintues)/1440)
    
    final_result_min = result_mintues%60
    final_result_hour = int((result_mintues - final_result_min)/60)
    
    if final_result_hour > 11 :
        time = "PM"
        final_result_hour = final_result_hour - 12
        if final_result_hour == 0 :
            final_result_hour = 12
    else :
        time = "AM"
        if final_result_hour == 0 :
            final_result_hour = 12
    
    if param != "" :
        n = weekday.index(param) + 1
        n = n + whole_day
        n = n%7 - 1
        to_print = str(final_result_hour)+":"+str(final_result_min)+" "+str(time)+", "+weekday[n].title()
    else :
        to_print = str(final_result_hour)+":"+str(final_result_min)+" "+str(time)
    
    if whole_day > 0 :
        if whole_day == 1 :
            to_print = to_print+" "+"(next day)"
        else :
            to_print = to_print+" ("+str(whole_day)+" days later)"
    print(to_print)
    

given1 = "11:23 PM"
given2 = "25:00"
add_time(given1, given2,"Saturday")


