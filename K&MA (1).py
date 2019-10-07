# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:27:56 2019

@author: Bright
"""
import subprocess
from IPython.core.pylabtools import figsize
import haohaninfo
from haohaninfo import GOrder
import time
# 取報價部分
import tailer
import matplotlib.pyplot as plt
from time import gmtime, strftime
import numpy as np



x = GOrder.GOQuote()
#y0=x.DescribeLast('Capital','match','TX09')
#print(y0)
time.sleep(2)

##################當前時間----秒
def currenttime():
    sec=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2][1])
    return sec
##################
##################當前時間----分
def currenttime():
    Cmin=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1][1])
    return Cmin
##################
    
XX=[]
Y=[0,0]
Z=[0,0]
openclose=[]
price2=[0,0]

def MinK():
    print('start')
    openprice=0
    closeprice=0
    while(1>0):
        #y0=x.DescribeLast('Capital','match','TX09')

        HR=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[0].split(' ')[1])#小時        
        #***此處篩選標準待修改***
        Cmin1=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1][1])
        Csec1=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2][1])
        print(Cmin1)
        print(Csec1)
        print('===')
        y=x.DescribeLast('Capital','match','TX09')
        Cmin2=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1][1])
        Csec2=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2][1])  
        print(Cmin1)
        print(Csec2)
        
        price2[0]=price2[1]
        price2[1]=int(y[2])
        
        if len(openclose)==0 :
            if(Cmin1!=Cmin2 and Cmin2<1):
                price2[0]=y[2]
                Y[0]=price2[0]
                print('Y=',Y)
        if len(openclose)!=0 :
            if(Cmin1!=Cmin2):
                if(Cmin1==4):
                    Y[1]=price2[0]
                    Z[0]=price2[1]
                    print('Y=',Y)
                    print('Z=',Z)
                if(Cmin1==9):
                    Z[1]=price2[0]
                    XX.append(Y)
                    XX.append(Z)
                    Y[0]=price2[1]
                    print('Y=',Y)
                    print('Z=',Z)
        print(XX)
        print('=============')
                    
                    
                
            
        
        
        
        
        
        
        
        '''
        if(int(y0min=y0[0].split(':')[1][1])==4 and int(y0sec)==59 and int(y1min=y1[0].split(':')[1][1])==5 and int(y1sec)==0):
        if(int(y0min=y0[0].split(':')[1][1])==9 and int(y0sec)==59 and int(y1min=y1[0].split(':')[1][1])==0 and int(y1sec)==0):
        '''   
        
        
'''        
        if(sec==30):
            print('min1[1]=',int(min1[1]),'sec=',sec)  
            print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            time.sleep(1)

        
        if(int(min1[1])==0 and sec==0):
            print('get0open')
            time.sleep(1)
            openprice=int(y0[2])
            print(openprice)
            time.sleep(1)
        if(int(min1[1])==4 and sec==59):
            print('get5close')
            closeprice=int(y0[2])
            a=[openprice,closeprice]
            #print(a)
            X.append(a)
            time.sleep(1)

            
        if(int(min1[1])==5 and sec==0):
            print('get6open')
            openprice=int(y0[2])
            print(openprice)
            time.sleep(1)
        if(int(min1[1])==9 and sec==59):
            print('get9close')            
            closeprice=int(y0[2])
            a=[openprice,closeprice]
            #print(a)
            X.append(a)   
            time.sleep(1)
'''    
    
    
    
'''    
        if(HR+8==15 and int(min1)==31):
            haohaninfo.GOrder.GOQuote().EndDescribe ()
            return X
'''
print(MinK())
    
