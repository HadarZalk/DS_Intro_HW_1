#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Task A 	 Write a function named my_func(x1, x2, x3) that returns the value: ((x1+x2 + x3)*(x2+x3)*x3)/(x1+x2+x3)


# In[55]:


x1= input("input a float number ")
x2= input("input a float number ")
x3= input("input a float number ")
try:
    x1=float(x1)
    x2=float(x2)
    x3=float(x3)
except:
    print ('Error: parameters should be float')
        
def My_Func (x1,x2,x3):
    b=(x1+x2+x3)
    if b == 0:
        print ("Not a number – denominator equals zero")
    else:
        while True:
            try:
                y= ((x1+x2+x3)*(x2+x3)*x3)/b
                return (float(y))
                break
            except ValueError:
                print ('None')


# In[56]:


My_Func (x1,x2,x3)


# In[57]:


# Task B 	 Write a function named convert(hours, minutes) that takes two number and converts them to seconds


# In[89]:


hours = float(input('enter an hour you would like to convert '))
minutes = float(input('enter a minutes you would like to convert '))
if hours <= 0 :
    print ('input error')

def Convert (hours, minutes):
    hours *=3600
    minutes *=60
    print(f'the hours convert to seconds: {hours},\nthe mintues convert to seconds {minutes},\nhours and mintues are {hours+minutes} seconds')
    


# In[90]:


Convert (hours, minutes)


# In[ ]:





# In[ ]:




