# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:42:45 2016

@author: p2admin
"""
class Employee:
    raise_amt=1.04
   
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@gmail.com'
        self.pay=pay
    def full_name(self):
        return '{}{}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

### dunder repr printing employee object
# trying to print a string that can recreate the obejct
    def __repr__(self):
        return "Employee('{}','{}', {})".format(self.first,self.last,self.pay) 

# dunder str method

    def __str__(self):
           return "Employee('{}','{}', {})".format(self.first,self.last,self.email) 


### defines how to add two objects
    def __add__(self,other):
        return(self.pay+other.pay)
### dunder len methods
    def __len__(self):
        return len(self.full_name())
emp1=Employee('Deepak','k',160000)
emp2=Employee('Deepa','k',60000)



#### dunder
print(emp1)
print(repr(emp1))
print(str(emp1))



#  ADDing two objects
#print(int.__add__(1,2)) # dunder add method
#print(str.__add__('1','2'))
### calling dunder method to add two objects
print(emp1+emp2)


### finding length
print(len('test')) # is same as
print('test'.__len__())
print(len(emp1))


### real world examples


#import time as time

