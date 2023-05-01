# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 21:49:41 2023

@author: johnm
"""
#instructions
#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

class Rectangle:
 
    def __init__(self,width,height):
            self.to_print = []
            self.set_width(width)
            self.set_height(height)
 
    def __str__(self):
        return self.__class__.__name__+"(width="+str(self.width)+", height="+str(str(self.height))+")"
 
    def set_width(self,width):
        self.width = width
    
    def get_width(self):
        return self.width
        
    def set_height(self,height):
        self.height = height
        
    def get_height(self):
        return self.height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)** 0.5
    
    def get_picture(self):
        if self.width < 50 and self.height < 50:
            h = 0
            w = 0
            to_print = ""
            while h < self.height:
                to_add = ""
                w = 0
                while w < self.width:
                    to_add = to_add + "*"
                    w = w+1
                
                to_add = to_add + "\n"
            
                to_print = to_print + to_add
                h = h+1
            return to_print
        else:
            return "Too big for picture."

    def get_amount_inside(self,square):
        return int(self.width/square.get_width())*int(self.height/square.get_height())

class Square(Rectangle):
    def __init__(self, side):
        if side < 50 :
            self.width = side
            self.height = side
        else : 
            return "Too big for picture."
        
    def __str__(self):
        return self.__class__.__name__+"(side="+str(self.width)+")"
        
    def set_side(self,side):
        self.width = side
        self.height = side
        
    def set_width(self,width):
        self.width = width
        self.height = width
        
    def set_height(self,height):
        self.height = height
        self.width = height
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_amount_inside(self,rectangle):
        return int(self.width/rectangle.get_width())*int(self.height/rectangle.get_height())
    
        
        

