import matplotlib.pyplot as plt
from time import gmtime, strftime
import numpy as np
import csv

#print('1')

x = GOrder.GOQuote()
y0=x.DescribeLast('Capital','match','TX10')
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
#得到內外盤的量  11分鐘的值是要看是不是盤整或是有禮到進場，總量則是看趨勢
'''
#若是從盤中開始看則要先設定目前價與量，不然總量會有錯!!!!!!!!!!!!!
outpan=1230 #外盤起始值  誤差  少
inpan=1530 #內盤起始值   誤差  少
p=[0,0]#成交價
Q=[inpan+outpan,0]#成交量
in11list=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0]
out11list=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0]
allin=[]
infivesum=[]
allout=[]
outfivesum=[]
#allin2=[]
#allout2=[]
#allin3=[]
#allout3=[]

print('對比價格',p[0],p[1])
print('start')
if p[0]==0:
   p[0]=int(x.DescribeLast('Capital','match','TX10')[2])
   while 1>0:
       if int(x.DescribeLast('Capital','match','TX10')[2])!=p[0] and p[1]==0:
           p[1]=int(x.DescribeLast('Capital','match','TX10')[2])
           break
       

print('對比價格',p[0],p[1])
        
def the11inout(inpan,outpan,inlist,outlist):
    Cmin1=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1] #分鐘，str
    Csec1=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2] #秒鐘，str
            
    i=x.DescribeLast('Capital','match','TX10')
            
    Cmin2=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1]
    Csec2=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2]
    
    HR=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[0].split(' ')[1])+8 #小時
    if HR>=24:
        HR=HR-24
    
    if Cmin1 != Cmin2:
        print([HR,Cmin1,outlist[10]])
        print('HR=',HR)
        
        if outlist[9]!=-1:#outlist 寫入CSV並且第一個資料不計入
            with open('AllMinoutAM.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([HR,Cmin1,outlist[10]])
                
                    
        
        print('-------------------')
        print(outlist[0],outlist[1],outlist[2],outlist[3],outlist[4],outlist[5],outlist[6],outlist[7],outlist[8],outlist[9],outlist[10])
        if(outlist[10]!=0):
            allout.append(outlist[10])  
            print("allout lenth",len(allout))  
            if len(allout)>4 :   
               outfivesum.append([HR,Cmin2,allout[-1]+allout[-2]+allout[-3]+allout[-4]+allout[-5]]) 
               with open('outfivesum.csv', 'a', newline='') as csvFile:
                   writer = csv.writer(csvFile)
                   writer.writerow(outfivesum[-1])
                
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
        
          
        
        if inlist[9]!=-1:#inlist 寫入CSV並且第一個資料不計入
            with open('AllMininAM.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([HR,Cmin2,inlist[10]])
                
                    
        print(inlist[0],inlist[1],inlist[2],inlist[3],inlist[4],inlist[5],inlist[6],inlist[7],inlist[8],inlist[9],inlist[10])
        print('-------------------')
        if(inlist[10]!=0):
            print("inlist lenth",len(inlist))
            allin.append(inlist[10])
            if len(allout)>4 :   
               infivesum.append([HR,Cmin2,allin[-1]+allin[-2]+allin[-3]+allin[-4]+allin[-5]]) 
               with open('infivesum.csv', 'a', newline='') as csvFile:
                   writer = csv.writer(csvFile)
                   writer.writerow(infivesum[-1])
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
             
        
        
    #----------------------------------  
    if int(i[2])!=p[1]:
        if int(i[2])>p[1]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            outpan+=inamount
            outlist[10]+=inamount
            print('外盤增加',inamount)
            #print('外盤:'+str(outpan))
            #print('總量='+str(inpan+outpan))
            #print('內盤:'+str(inpan))
#            if(outpan!=0 and inpan!=0):
#                print('內外盤比'+str(outpan/(inpan+outpan)))
#                print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
        
        if int(i[2])<p[1]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            inpan+=inamount
            inlist[10]+=inamount
            print('內盤增加',inamount)
            #print('內盤:'+str(inpan))                      
            #print('總量='+str(inpan+outpan))
            #print('外盤:'+str(outpan))
#            if(outpan!=0 and inpan!=0):
#                print('內外盤比'+str(outpan/(inpan+outpan)))
#                print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))                
    if int(i[2])==p[1]:
        if int(i[2])>p[0]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            outpan+=inamount
            outlist[10]+=inamount
            print('外盤增加',inamount)
            #print('外盤:'+str(outpan))                    
            #print('總量='+str(inpan+outpan))
            #print('內盤:'+str(inpan))
#            if(outpan!=0 and inpan!=0):
#                print('內外盤比'+str(outpan/(inpan+outpan)))
#                print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
                    
        if int(i[2])<p[0]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            inpan+=inamount
            inlist[10]+=inamount
            print('內盤增加',inamount)
            #print(p[0],p[1])
            #print('內盤:'+str(inpan))
            #print('總量='+str(inpan+outpan))
            #print('外盤:'+str(outpan))
#            if(outpan!=0 and inpan!=0):
#                print('內外盤比'+str(outpan/(inpan+outpan)))
#                print('外盤/內盤'+str(outpan/inpan)+'  內盤/外盤'+str(inpan/outpan))
    print('對比價格',p[0],p[1])
    if int(i[2])!=p[1]:
        p[0]=p[1]
        p[1]=int(i[2]) 
    Q[0]=Q[1]


while 1>0:
    the11inout(inpan,outpan,in11list,out11list)