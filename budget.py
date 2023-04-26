# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:28:49 2023

@author: johnm
"""

class Category(object) :
    ledger = []
    temp = 0
    category_name = ""
    temp_print = ""
    def __init__(self,name):
        self.category_name = name
    
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
    
wee = Category("haha")
wee.deposit(100,"try only")
wee.deposit(100,"another try only1")
wee.deposit(100,"another try only2")
wee.deposit(100,"another try only3")
wee.deposit(100,"another try only4")
wee.withdraw(200,"cp")
wee.print()
