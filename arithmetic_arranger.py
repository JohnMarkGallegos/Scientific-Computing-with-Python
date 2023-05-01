# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:06:27 2023

@author: johnm
"""
#instructions
#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def arithmetic_arranger(input_list,arg=False): 
    first_digits_output = []
    second_digits_output = []
    result_digits_output = []

    dash_output = []
    count = 0
    final_first = ""
    final_second = ""
    final_dash = ""
    final_result = ""
    if len(input_list) > 5 :
        print("Error : Too many problems.")
        return
    else :
        for n in input_list:
            if "+" in n or "-" in n :
                if "+" in n :
                    if n.split('+')[0].strip().isdigit() and n.split('+')[1].strip().isdigit() :
                        if len(n.split('+')[0].strip()) > 4 or len(n.split('+')[1].strip()) > 4 :
                            print("Error: Numbers cannot be more than four digits.")
                            return
                        else :
                            temp = max(len(n.split('+')[0].strip()),len(n.split('+')[1].strip()))
                            
                            if temp == len(n.split('+')[0].strip()) :
                                count2 = 0
                                first_digits_output.append("  "+n.split('+')[0].strip())
                                second_digits_output.append(n.split('+')[1].strip())
                                dash_output.append('-')
                                result_digits_output.append(str(int(n.split('+')[0].strip())+int(n.split('+')[1].strip())))
                                
                                
                                while count2 < temp - 1 - len(n.split('+')[1].strip()) +2 :
                                    second_digits_output[count] = " "+second_digits_output[count]
                                    count2 = count2 + 1
                                    
                                
                                second_digits_output[count] = "+"+second_digits_output[count]
                                count2 = 0
                                while count2 < temp +1 :
                                    dash_output[count] = "-"+dash_output[count]
                                    count2 = count2 + 1
                                    
                                count2 = 0
                                while count2 < temp + 3 - len(result_digits_output[count]) :
                                    result_digits_output[count] = " "+result_digits_output[count]
                                    count2 = count2 + 1
                                
                            else :
                                count2 = 0
                                first_digits_output.append(n.split('+')[0].strip())
                                second_digits_output.append("+ "+n.split('+')[1].strip())
                                dash_output.append('-')
                                result_digits_output.append(str(int(n.split('+')[0].strip())+int(n.split('+')[1].strip())))
                                
                                while count2 < temp -len(n.split('+')[0].strip())+2 :
                                    first_digits_output[count] = " "+first_digits_output[count]
                                    count2 = count2 + 1
                                
                                count2 = 0
                                while count2 < temp +1 :
                                    dash_output[count] = "-"+dash_output[count]
                                    count2 = count2 + 1
                            
                                count2 = 0
                                while count2 < temp + 3 - len(result_digits_output[count]) :
                                    result_digits_output[count] = " "+result_digits_output[count]
                                    count2 = count2 + 1
                    else :
                        print("Error : Numbers must only contain digits.")    
                        return
                if "-" in n :
                    
                    if n.split('-')[0].strip().isdigit() and n.split('-')[1].strip().isdigit() :
                        if len(n.split('-')[0].strip()) > 4 or len(n.split('-')[1].strip()) > 4 :
                            print("Error: Numbers cannot be more than four digits.")
                            return
                        else :
                            temp = max(len(n.split('-')[0].strip()),len(n.split('-')[1].strip()))
                            
                            if temp == len(n.split('-')[0].strip()) :
                                count2 = 0
                                first_digits_output.append("  "+n.split('-')[0].strip())
                                second_digits_output.append(n.split('-')[1].strip())
                                dash_output.append('-')
                                result_digits_output.append(str(int(n.split('-')[0].strip())-int(n.split('-')[1].strip())))
                                
                                while count2 < temp - 1 - len(n.split('-')[1].strip()) +2 :
                                    second_digits_output[count] = " "+second_digits_output[count]
                                    count2 = count2 + 1
                                    
                                
                                second_digits_output[count] = "-"+second_digits_output[count]
                                count2 = 0
                                while count2 < temp +1 :
                                    dash_output[count] = "-"+dash_output[count]
                                    count2 = count2 + 1
                                    
                                count2 = 0
                                while count2 < temp + 3 - len(result_digits_output[count]) :
                                    result_digits_output[count] = " "+result_digits_output[count]
                                    count2 = count2 + 1
                            else :
                                count2 = 0
                                first_digits_output.append(n.split('-')[0].strip())
                                second_digits_output.append("- "+n.split('-')[1].strip())
                                
                                dash_output.append('-')
                                result_digits_output.append(str(int(n.split('-')[0].strip())-int(n.split('-')[1].strip())))
                                while count2 < temp - 1 -len(n.split('-')[0].strip())+3 :
                                    first_digits_output[count] = " "+first_digits_output[count]
                                    count2 = count2 + 1
                                
                                count2 = 0
                                while count2 < temp +1 :
                                    dash_output[count] = "-"+dash_output[count]
                                    count2 = count2 + 1   
                                    
                                count2 = 0
                                while count2 < temp + 3 - len(result_digits_output[count]) :
                                    result_digits_output[count] = " "+result_digits_output[count]
                                    count2 = count2 + 1
                    else :
                        print("Error : Numbers must only contain digits.")    
                        return
                
            else :
                print("Error : Operator must be '+' or '-'.")
                return
            count = count + 1
        
        count = 0
        
        while count < len(first_digits_output):
            final_first = final_first + first_digits_output[count]+"    "
            final_second = final_second + second_digits_output[count]+"    "
            final_dash = final_dash + dash_output[count]+"    "
            final_result = final_result + result_digits_output[count] + "    "
            count = count + 1
        
        print(final_first)
        print(final_second)
        print(final_dash)
        if arg == True :
            print(final_result)
        
given1 = ['3801 - 2', '123 + 49']
given2 = ['1 + 2', '1 - 9380']
given3 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
given4 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
given5 = ['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']
given6 = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
given7 = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
given8 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
given9 = ['3 + 855', '988 + 40'] #True
given10 = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'] #True
arithmetic_arranger(given10,True)
