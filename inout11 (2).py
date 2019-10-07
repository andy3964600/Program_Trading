# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:23:02 2019

@author: Bright

#===========================內外盤比 與委買委賣
內外盤差+比 OK
委買委賣 
MA跟K
1分鐘之交易量+累計交易量

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

#print('1')

x = GOrder.GOQuote()
y0=x.DescribeLast('Capital','match','TX09')
'''
y1=x.Describe('Capital','updn5','TXO10500I9')  
#y1=x.Describe('Simulator','updn5','TXFI9')  
for i in y1:
    print(i) 
'''
##################當前時間
millis = int(round(time.time() * 1000))
##################當前時間----秒
def currenttime():
    sec=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2])
    return sec
##################
'''
#取得每個11分鐘之內外盤數據，若是小於59秒則判定為前一時段之內外盤量，若是跨秒則定義為下一分鐘之內外盤。啟示之內外盤陣列都是0用append丟進去

'''
#若是從盤中開始看則要先設定目前價與量，不然總量會有錯!!!!!!!!!!!!!
outpan=1380 #外盤起始值  誤差  少
inpan=1800 #內盤起始值   誤差  少
p=[10410,0]#成交價
Q=[inpan+outpan,0]#成交量
in11list=[0,0,0,0,0,0,0,0,0,0,0]
out11list=[0,0,0,0,0,0,0,0,0,0,0]
allin1=[]
allout1=[]
#allin2=[]
#allout2=[]
#allin3=[]
#allout3=[]

#起始if用牌判定一個變化是內或外
for ii in y0:
    if int(ii[2])>p[0]:
        outpan+=1
        p[1]=int(ii[2])
        print('外盤:'+str(outpan))
        print('總量='+str(inpan+outpan))
        break
    if int(ii[2])<p[0]:
        inpan +=1
        p[1]=int(ii[2])
        print('內盤:'+str(inpan))
        print('總量='+str(inpan+outpan))
        break
    
    
#後續的iF用來判斷內或外，並且如果跳分(min1!=min2)則將上一分鐘之內外盤做總結。Q陣列為價 P陣列為量
    #####################################
def the11inout(inpan,outpan,inlist,outlist):
    while(1>0):
        print('123456')
        if(millis/1000>1566873620):
            print('========================================================================================')
            min1=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1]) 
            csec=currenttime()
            if(csec<=59): 
                print(csec)
                i=x.DescribeLast('Capital','match','TX09')   
                print(i)
                Q[1]=int(i[4])        
                if int(i[2])!=p[1]:
                    p[0]=p[1]
                    #print('K1')
                    if int(i[2])>p[1]:
                        inamount=int(Q[1])-Q[0]
                        outpan+=inamount
                        outlist[10]+=inamount
                        print('外盤:'+str(outpan))
                        print('總量='+str(inpan+outpan))
                        print('內盤:'+str(inpan))
                        if(outpan!=0 and inpan!=0):
                            print('內外盤比'+str(outpan/(inpan+outpan)))
                            print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
                    
                    if int(i[2])<p[1]:
                        inamount=int(Q[1])-Q[0]
                        inpan+=inamount
                        inlist[10]+=inamount
                        print('內盤:'+str(inpan))                      
                        print('總量='+str(inpan+outpan))
                        print('外盤:'+str(outpan))
                        if(outpan!=0 and inpan!=0):
                            print('內外盤比'+str(outpan/(inpan+outpan)))
                            print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))                
                if int(i[2])==p[1]:
                    if int(i[2])>p[0]:
                        inamount=int(Q[1])-Q[0]
                        outpan+=inamount
                        outlist[10]+=inamount
                        print('外盤:'+str(outpan))                    
                        print('總量='+str(inpan+outpan))
                        print('內盤:'+str(inpan))
                        if(outpan!=0 and inpan!=0):
                            print('內外盤比'+str(outpan/(inpan+outpan)))
                            print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
                                
                    if int(i[2])<p[0]:
                        inamount=int(Q[1])-Q[0]
                        inpan+=inamount
                        inlist[10]+=inamount
                        #print(p[0],p[1])
                        print('內盤:'+str(inpan))
                        print('總量='+str(inpan+outpan))
                        print('外盤:'+str(outpan))
                        if(outpan!=0 and inpan!=0):
                            print('內外盤比'+str(outpan/(inpan+outpan)))
                            print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
                p[1]=int(i[2]) 
                Q[0]=Q[1]
                min2=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1])
                
            #資料迭代，並將上一時段之內外盤丟到陣列中。   
            if(min1!=min2):
                print(outlist[0],outlist[1],outlist[2],outlist[3],outlist[4],outlist[5],outlist[6],outlist[7],outlist[8],outlist[9],outlist[10])
                if(outlist!=0):
                    allout1.append(outlist[10])                
                outlist[0]=outlist[1]
                outlist[1]=outlist[2]
                outlist[2]=outlist[3]
                outlist[3]=outlist[4]
                outlist[4]=outlist[5]
                outlist[5]=outlist[6]
                outlist[6]=outlist[7]
                outlist[7]=outlist[8]
                outlist[8]=outlist[9]
                outlist[9]=outlist[10]
                outlist[10]=0
                
                print(inlist[0],inlist[1],inlist[2],inlist[3],inlist[4],inlist[5],inlist[6],inlist[7],inlist[8],inlist[9],inlist[10])
                if(inlist[10]!=0):
                    allin1.append(inlist[10])
                inlist[0]=inlist[1]
                inlist[1]=inlist[2]
                inlist[2]=inlist[3]
                inlist[3]=inlist[4]
                inlist[4]=inlist[5]
                inlist[5]=inlist[6]
                inlist[6]=inlist[7]
                inlist[7]=inlist[8]
                inlist[8]=inlist[9]
                inlist[9]=inlist[10]
                inlist[10]=0
                print("allout1 lenth",len(allout1))
                X=30
        if(len(allout1)>X):  #用來檢查用，如果所有內外盤價格陣列長度過X則結束訂閱並跳出
            allout1[0]=0
            allin1[0]=0             
            haohaninfo.GOrder.GOQuote().EndDescribe ()
            break
    return allout1,allin1   
        

        
#1566799199
#millis/1000 < 1566813507

    #print('========================================================================================')
print(millis/1000)
the11inout(inpan,outpan,in11list,out11list)    
    
    
   
       
print('Loop end')
if(type(the11inout(inpan,outpan,in11list,out11list)) != 'NoneType'):
    Allout,Allin=the11inout(inpan,outpan,in11list,out11list)    

        
    
#plt.plot(outlist)
#plt.xlabel('out11')
#print('========================================================================================')
my_x_ticks = np.arange(0, 60, 1)#坐標軸數量
print(Allout,Allin)
plt.xticks(my_x_ticks)
plt.plot(Allout)
plt.xlabel('out-all')
print('========================================================================================')
figsize(17,10)
plt.plot(Allin)
plt.xlabel('in-a11')
print('========================================================================================')
 

#選擇權  
''' 
y1=x.Describe('Capital','match','TXO10500I9')  
for i in y1:
    print(i)
'''
       
    