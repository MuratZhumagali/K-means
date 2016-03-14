import math
import random

f = open('km-data.txt', 'r')  
l = []

for i in f: 
    i = i.split(',')
    l.append([float(i[0]), float(i[1])])
 
oldcenter1=l[random.randrange(150)]
oldcenter2=l[random.randrange(150)]
oldcenter3=l[random.randrange(150)]
print('Original centers')
print(oldcenter1)
print(oldcenter2)
print(oldcenter3)
def euclidean(center):
    Result=[]
    for i in l:
        L2=math.sqrt(math.pow(center[0]-i[0],2)+math.pow(center[1]-i[1],2))
        Result.append(L2)
    return Result
    
oldDistance1=euclidean(oldcenter1)
oldDistance2=euclidean(oldcenter2)
oldDistance3=euclidean(oldcenter3)

oldideallist1=[]
oldideallist2=[]
oldideallist3=[]
i=0
while i<len(oldDistance1):
    if (min(oldDistance1[i], oldDistance2[i], oldDistance3[i]))==oldDistance1[i]:
        oldideallist1.append(l[i])
    elif (min(oldDistance1[i], oldDistance2[i], oldDistance3[i]))==oldDistance2[i]:
        oldideallist2.append(l[i])
    else:
        oldideallist3.append(l[i])
    i=i+1

def Centercalc(ideallist):
    center=[]
    index=0
    x=0
    y=0
    while index<len(ideallist):
        x=x+ideallist[index][0]
        y=y+ideallist[index][1]
        index=index+1
    x=x/index
    y=y/index
    center.append(x)
    center.append(y)
    return center

newcenter1=Centercalc(oldideallist1)
newcenter2=Centercalc(oldideallist2)
newcenter3=Centercalc(oldideallist3)
print('After 1 iteration')
print(newcenter1)
print(newcenter2)
print(newcenter3)

count=1
while(1):
    if (newcenter1==oldcenter1) and (newcenter2==oldcenter2) and (newcenter3==oldcenter3):
        print('Stop')
        break
    else:
        count=count+1  
        newDistance1=euclidean(newcenter1)
        newDistance2=euclidean(newcenter2)
        newDistance3=euclidean(newcenter3)
        oldcenter1=newcenter1
        oldcenter2=newcenter2
        oldcenter3=newcenter3
        newideallist1=[]
        newideallist2=[]
        newideallist3=[]
        j=0
        while j<len(newDistance1):
            if (min(newDistance1[j], newDistance2[j], newDistance3[j]))==newDistance1[j]:
                newideallist1.append(l[j])
            elif (min(newDistance1[j], newDistance2[j], newDistance3[j]))==newDistance2[j]:
                newideallist2.append(l[j])
            else:
                newideallist3.append(l[j])
            j=j+1
        
        newcenter1=Centercalc(newideallist1)
        newcenter2=Centercalc(newideallist2)
        newcenter3=Centercalc(newideallist3)
        print('After', count, 'iteration')
        print('Kcenter1=',newcenter1, 'Klist1=',newideallist1)
        print('Kcenter2=',newcenter2, 'Klist2=',newideallist2)
        print('Kcenter3=',newcenter3, 'Klist3=',newideallist3) 