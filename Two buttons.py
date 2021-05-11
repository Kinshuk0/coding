# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:29:11 2021

@author: 007ki
"""

a=input()
A=a.split()
n=int(A[0])
m=int(A[1])
count=0
temp=n 
if n>m:
    count=n-m
    print(count)
else:
    if n==m:    
        print(count)
    else:
        if n==1 and m==2:
            print(1)
        elif m%n==0:
            count=m/n
            print(int(count))
        elif m/2>temp:
            while temp<m:
                temp=temp*2
                count=count+1
            count=count+1
            midistn=min(int(temp/2-m/2),temp-m)
            count=count+midistn
            print(int(count))
        elif m/2==temp:
            count=count+1
            print(count)
        else:
            count=count+1
            if int(temp-m/2)==temp-m/2:
              midistn=min(int(temp-m/2),temp*2-m)
              count=count+midistn
              print(int(count))
            else:
              midistn=min(int(temp-m/2)+1,temp*2-m)
              count=count+midistn
              print(int(count)) 
        
            
    