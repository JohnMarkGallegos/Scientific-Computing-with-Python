# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:12:32 2023

@author: johnm
"""
import random


class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for value in kwargs.items():
            n = 0
            while n < value[1]:
                self.contents.append(value[0])
                n = n+1
        self.duplicate = self.contents.copy()

    def draw(self,draw):
        n = min(len(self.duplicate),draw)
        r = 0
        self.drawn = []
        self.contents = self.duplicate.copy()
        while n > 0:
            r = random.randint(0, len(self.contents)-1)
            self.drawn.append(self.contents[r])
            self.contents.pop(r)
            n=n-1
        return self.drawn
      
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    n = 0
    success = 0
    while n < num_experiments:
        success_temp = 0
        drawn = hat.draw(num_balls_drawn)
        for p in expected_balls.items():
            if drawn.count(p[0]) >= p[1]:
                
                success_temp = success_temp + 1
        if success_temp == len(expected_balls):
            success = success + 1
        n=n+1
    return success/num_experiments