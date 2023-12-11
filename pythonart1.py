import bpy
import random

#Sets all lights to 0 at frame 0
for obj in bpy.context.selected_objects:
    obj.location.x=0
    obj.location.y=0
    obj.location.z=-1.7
    obj.keyframe_insert(data_path="location",frame=0)

#Explodes lights out randomly at frame 60
for obj in bpy.context.selected_objects:
    obj.location.x=random.uniform(-15,15)
    obj.location.y=random.uniform(0,15)
    obj.location.z=random.uniform(-2,15)
    obj.keyframe_insert(data_path="location",frame=60)
    obj.keyframe_insert(data_path="location",frame=110)

selObj = []
#BEFORE STARTING YOU HAVE TO SELECT ALL OBJECTS
#THIS CREATES AN LIST OF SELECTED OBJECTS
for obj in bpy.context.selected_objects:
    selObj.append(obj.name)

x=0
y=-2
z=0
h=1
w=.5
midLine = [[x,y,z+(.5*h)],[x+(.85*w),y,z+(.5*h)],[x+(.75*w),y,z+(.5*h)],[x+(.50*w),y,z+(.5*h)],[x+(.25*w),y,z+(.5*h)],[x+(.15*w),y,z+(.5*h)],[x+w,y,z+(.5*h)]]
topLine = [[x,y,z+h],[x+(.95*w),y,z+h],[x+(.90*w),y,z+h],[x+(.75*w),y,z+h],[x+(.65*w),y,z+h],[x+(.5*w),y,z+h],[x+(.45*w),y,z+h],[x+(.25*w),y,z+h],[x+(.15*w),y,z+h],[x+(.10*w),y,z+h],[x+w,y,z+h]]
bottomLine = [[x,y,z],[x+(.95*w),y,z],[x+(.75*w),y,z],[x+(.65*w),y,z],[x+(.50*w),y,z],[x+(.35*w),y,z],[x+(.25*w),y,z],[x+(.15*w),y,z],[x+w,y,z]]
leftLine = [[x,y,z],[x,y,z+(.05*h)],[x,y,z+(.15*h)],[x,y,z+(.25*h)],[x,y,z+(.3*h)],[x,y,z+(.45*h)],[x,y,z+(.50*h)],[x,y,z+(.55*h)],[x,y,z+(.65*h)],[x,y,z+(.75*h)],[x,y,z+(.85*h)],[x,y,z+(.95*h)],[x,y,z+h]]
rightLine = [[x+w,y,z],[x+w,y,z+(.05*h)],[x+w,y,z+(.15*h)],[x+w,y,z+(.25*h)],[x+w,y,z+(.35*h)],[x+w,y,z+(.50*h)],[x+w,y,z+(.65*h)],[x+w,y,z+(.75*h)],[x+w,y,z+(.85*h)],[x+w,y,z+(.95*h)],[x+w,y,z+h]]
tophalfRight = [[x+w,y,z+(.50*h)],[x+w,y,z+(.7*h)],[x+w,y,z+(.8*h)],[x+w,y,z+(.9*h)],[x+w,y,z+h]]
tophalfLeft = [[x,y,z+(.50*h)],[x,y,z+(.7*h)],[x,y,z+(.8*h)],[x,y,z+(.9*h)],[x,y,z+h]]
vertmidLine = [[x+(.5*w),y,z],[x+(.5*w),y,z+(.15*h)],[x+(.5*w),y,z+(.25*h)],[x+(.5*w),y,z+(.35*h)],[x+(.5*w),y,z+(.5*h)],[x+(.5*w),y,z+(.65*h)],[x+(.5*w),y,z+(.75*h)],[x+(.5*w),y,z+(.95*h)],[x+(.5*w),y,z+h]]

#REFERENCE COORDINATES
hNest = leftLine + leftLine + rightLine + midLine
aNest = leftLine + rightLine + midLine + topLine
pNest = leftLine + topLine + midLine + tophalfRight
yNest = rightLine + bottomLine + midLine + tophalfLeft
lNest = leftLine + bottomLine
oNest = rightLine + bottomLine + topLine + leftLine
wNest = rightLine + bottomLine + leftLine + vertmidLine
eNest = bottomLine + topLine + midLine + leftLine
nNest = leftLine + leftLine + rightLine + topLine

#A Function to Print The Things
def printNest(nestName,objElem,xstart,zstart):
    devVal=.03
    i=0
    while i < len(nestName):
    obj = bpy.data.objects[selObj[objElem]]
    obj.location.x=nestName[i][0]+xstart
    obj.location.y=nestName[i][1]
    obj.location.z=nestName[i][2]-zstart
    objElem+=1
    i+=1
    f=70
    while f < 101:
    obj.location.x=obj.location.x+random.uniform(-(devVal),devVal)
    obj.location.y=obj.location.y+random.uniform(-(devVal),devVal)
    obj.location.z=obj.location.z+random.uniform(-(devVal),devVal)
obj.keyframe_insert(data_path="location",frame=f)
f+=10

happy = [hNest,aNest,pNest,pNest,yNest]
halloween = [hNest,aNest,lNest,lNest,oNest,wNest,eNest,eNest,nNest]

lenObj=0
x=-4
i=0

while i < len(happy):
printNest(happy[i],lenObj,x,0)
lenObj=lenObj+len(happy[i])
x+=w+(.5*w)
i+=1

x=-4
i=0
while i < len(halloween):
printNest(halloween[i],lenObj,x,1.5)
lenObj=lenObj+len(halloween[i])
x+=w+(.5*w)
i+=1
