# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:04:58 2016

@author: p2admin
"""
# Duck typing= pythonic. Non pythinic-. we dont care about what kind of objects we are workig with. we dont care if the objects 

class Duck:
    def quack(self):
        print('Quack,Quack')
    def fly(self):
        print('Fllap!,Flap!')
    
    
class Person:
    def quack(self):
        print('Quack,Quack! like a Duck')
    def fly(self):
        print('Fllap!,Flap! like a Duck')

# we dont care what kind of objects it is we only if it can quack and fly.
# general function
def quack_and_fly(thing):
    
 # Non-pythonic way    dont do this
#    if isinstance(thing,Duck):
#        thing.quack()
#        thing.fly()
#    else:
#        print("This has to be a duck")        


# EAFP (pythonic way).. try to ask for forgiveness if you make a mistake
    try:
        thing.quack()
        thing.fly()
        #thing.bark()
    except AttributeError as e:
        print(e)        
    


d=Duck()
#quack(d)
quack_and_fly(d)

p=Person()
quack_and_fly(p)



### Example 2

person={'name':'Deepak', 'age':26}
person={'name':'Deepak', 'age':26, 'job':'programmer'}


### Non Pythonic way
if ('name' in person and 'age' in person and 'job'in person):
    print("yes")

### EAFP pythonic way
try:
    print ("I'm {age} years old ".format(**person))
    print ("I'm {ages} years old ".format(**person))

except KeyError as e:
    print("Missing {} key".format(e))
    
    
### Example 3
    
my_list=[1,2,3,4,5,6]

#non-Pythonic way- Asking permissions

if (len(my_list)>=6):
    print (my_list[5])
else:
    print('That index does not exist')

### Pythonic way- Ask Forgiveness
try:
    print(my_list[7])
except IndexError as e:
    print(e)

######## why ask forgiveness? Why DUCK typing?
# ask permission is slower
# less readable
# pythonic way- try and excpet is more readable
 