# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:28:49 2023

@author: johnm
"""

class Category :

    def __init__(self,name):
        self.category_name = name
        self.ledger = []
        self.temp = 0
        self.temp_print = ""
    def get_category_name(self):
        return self.category_name
    
    def check_funds(self,amount) :
        self.temp = 0
        for n in self.ledger :
            self.temp = self.temp + n["amount"]
        
        self.temp = self.temp - amount
        if self.temp >= 0:
            return True
        else :
            return False
    
    def deposit(self,amount,description="") :
        self.ledger.append({"amount" : amount, "description" : description})
        
    def withdraw(self,amount,description="") :
        if self.check_funds(amount) :
            self.ledger.append({"amount" : -1*amount, "description" : description})
            return True
        else :
            return False
        
    def get_balance(self) :
        self.temp = 0
        for n in self.ledger :
            self.temp = self.temp + n["amount"]
        return self.temp
        
    def transfer(self,amount,class_cat) :
        if self.check_funds(amount) :
            self.ledger.append({"amount" : -1*amount, "description" : "Transfer to "+class_cat.category_name})
            class_cat.deposit(amount,"Transfer from "+self.category_name)
            return True
        else :
            return False
        
    def print(self) :
        self.temp = round((30 - len(self.category_name))/2)
        while self.temp > 0 :
            self.temp_print = self.temp_print + "*"
            self.temp = self.temp - 1
        self.temp_print = self.temp_print+self.category_name
        self.temp = 30 - len(self.temp_print)
        while self.temp > 0 :
            self.temp_print = self.temp_print + "*"
            self.temp = self.temp - 1
        print(self.temp_print)
        
        for n in self.ledger :
            self.temp_print = n["description"][0:23]
            
            while len(self.temp_print) <23 :
                self.temp_print = self.temp_print + " "
            
            self.temp = 7-len(str(format(n["amount"],'.2f')))
            while self.temp > 0 :
                self.temp_print = self.temp_print + " "
                self.temp = self.temp - 1
            self.temp_print = self.temp_print + str(format(n["amount"],'.2f'))
            print(self.temp_print)
    

def create_spend_chart(var) :
    spent = []
    count = 100
    to_add = ""
    to_print = ["Percentage spent by category"]
    for n in var:
        deposit = 0
        withdrawal = 0
        for m in n.ledger :
            if m["amount"] >= 0 :
                deposit = deposit + m["amount"]
            else :
                withdrawal = withdrawal + m["amount"]
        spent.append((n.get_category_name(),int((withdrawal/deposit)*-100)))
    
    while count >= 0 :
        to_add = ""
        to_add = str(count)+"| "
        
        while len(to_add) < 5 :
            to_add = " " + to_add
        
        for n in spent :
            if n[1] >= count :
                to_add = to_add + "o  "
            else :
                to_add = to_add + "   "
        to_print.append(to_add)
        count = count - 10
        
    to_add = ""
    
    while len(to_add) < 1+len(var)*3:
        to_add = to_add + "-"
        
    to_add = "    "+to_add
    to_print.append(to_add)
    
    max_char = 0
    for n in var:
        max_char = max(max_char,len(n.get_category_name()))
    
    count = 0
    while count < max_char:
        to_add = "     "
        for n in var :
            if len(n.get_category_name()) > count :
                to_add = to_add + n.get_category_name()[count] + "  "
            else:
                to_add = to_add + "   "
        to_print.append(to_add)
        count = count + 1
    
    for n in to_print:
        print(n)

