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
##################��e�ɶ�
millis = int(round(time.time() * 1000))
##################��e�ɶ�----��
def currenttime():
    sec=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2])
    return sec
##################
'''
#���o�C��11���������~�L�ƾڡA�Y�O�p��59��h�P�w���e�@�ɬq�����~�L�q�A�Y�O���h�w�q���U�@���������~�L�C�ҥܤ����~�L�}�C���O0��append��i�h
#�o�줺�~�L���q  11�������ȬO�n�ݬO���O�L��άO��§��i���A�`�q�h�O���Ͷ�
'''
#�Y�O�q�L���}�l�ݫh�n���]�w�ثe���P�q�A���M�`�q�|����!!!!!!!!!!!!!
outpan=1230 #�~�L�_�l��  �~�t  ��
inpan=1530 #���L�_�l��   �~�t  ��
p=[0,0]#�����
Q=[inpan+outpan,0]#����q
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

print('������',p[0],p[1])
print('start')
if p[0]==0:
   p[0]=int(x.DescribeLast('Capital','match','TX10')[2])
   while 1>0:
       if int(x.DescribeLast('Capital','match','TX10')[2])!=p[0] and p[1]==0:
           p[1]=int(x.DescribeLast('Capital','match','TX10')[2])
           break
       

print('������',p[0],p[1])
        
def the11inout(inpan,outpan,inlist,outlist):
    Cmin1=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1] #�����Astr
    Csec1=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2] #�����Astr
            
    i=x.DescribeLast('Capital','match','TX10')
            
    Cmin2=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[1]
    Csec2=strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[2]
    
    HR=int(strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(':')[0].split(' ')[1])+8 #�p��
    if HR>=24:
        HR=HR-24
    
    if Cmin1 != Cmin2:
        print([HR,Cmin1,outlist[10]])
        print('HR=',HR)
        
        if outlist[9]!=-1:#outlist �g�JCSV�åB�Ĥ@�Ӹ�Ƥ��p�J
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
        
          
        
        if inlist[9]!=-1:#inlist �g�JCSV�åB�Ĥ@�Ӹ�Ƥ��p�J
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
            print('�~�L�W�[',inamount)
            #print('�~�L:'+str(outpan))
            #print('�`�q='+str(inpan+outpan))
            #print('���L:'+str(inpan))
#            if(outpan!=0 and inpan!=0):
#                print('���~�L��'+str(outpan/(inpan+outpan)))
#                print('�~�L/���L'+str(outpan/inpan)+'  ���L/�~�L'+str(inpan/outpan))
        
        if int(i[2])<p[1]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            inpan+=inamount
            inlist[10]+=inamount
            print('���L�W�[',inamount)
            #print('���L:'+str(inpan))                      
            #print('�`�q='+str(inpan+outpan))
            #print('�~�L:'+str(outpan))
#            if(outpan!=0 and inpan!=0):
#                print('���~�L��'+str(outpan/(inpan+outpan)))
#                print('�~�L/���L'+str(outpan/inpan)+'  ���L/�~�L'+str(inpan/outpan))                
    if int(i[2])==p[1]:
        if int(i[2])>p[0]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            outpan+=inamount
            outlist[10]+=inamount
            print('�~�L�W�[',inamount)
            #print('�~�L:'+str(outpan))                    
            #print('�`�q='+str(inpan+outpan))
            #print('���L:'+str(inpan))
#            if(outpan!=0 and inpan!=0):
#                print('���~�L��'+str(outpan/(inpan+outpan)))
#                print('�~�L/���L'+str(outpan/inpan)+'  ���L/�~�L'+str(inpan/outpan))
                    
        if int(i[2])<p[0]:
            #inamount=int(Q[1])-Q[0]
            inamount=int(i[3])
            inpan+=inamount
            inlist[10]+=inamount
            print('���L�W�[',inamount)
            #print(p[0],p[1])
            #print('���L:'+str(inpan))
            #print('�`�q='+str(inpan+outpan))
            #print('�~�L:'+str(outpan))
#            if(outpan!=0 and inpan!=0):
#                print('���~�L��'+str(outpan/(inpan+outpan)))
#                print('�~�L/���L'+str(outpan/inpan)+'  ���L/�~�L'+str(inpan/outpan))
    print('������',p[0],p[1])
    if int(i[2])!=p[1]:
        p[0]=p[1]
        p[1]=int(i[2]) 
    Q[0]=Q[1]


while 1>0:
    the11inout(inpan,outpan,in11list,out11list)