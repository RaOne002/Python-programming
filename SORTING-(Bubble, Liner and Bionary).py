# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:14:08 2022

@author: subhr

"""
# BUBBLE SORTING @@@@@@@@@@@

print('Bubble sorting')

def bubble(a):
    n=len(a)
    
    
    for i in range(n):
        for j in range(0,n-i-1):
            if (a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp


a=[12, 4, 8, 27, 7, 9, 20]
bubble(a)

for i in a:
    print(i)
    
    
# Liner Search @@@@@@@@@@@

def liner_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    

    count=0
    flag=0
    for i in element:
        count=count+1
        if(i==x):
            print('Yes I found the number ',i)
            flag=1
            break
        
    if(flag==0):
        print('Number is not found')
    print('Number of iteration is',count)
    
    
    
 # BIONARY SEARCH @@@@@@@@@@@@@
 
def bionary_search (a, x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    
    while (first_pos<=last_pos and flag==0):
        count=count+1
        mid=(first_pos+last_pos)//2
        if (x==a[mid]):
            flag=1
            print('The number is present at pos',mid)
            print('The number of iterations is',count)
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
                
    print('Sorry number is not present')
    
        
    
        
        
a=[]
for i in range(1,1000):
    a.append(i)
    
bionary_search(a, 50)






