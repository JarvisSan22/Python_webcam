import numpy as np
import cv2 
import math
import datetime
from datetime import timedelta as Delta 
h=300
w=300
cap = cv2.VideoCapture(0)
SUN_LOC=(200,70)
SUN_RSIZE=20
ORBITAL_R=10



def Orbiral(frame,Centerloc,orbit_r,size_r,phi,color):
    
    x_orbit=Centerloc[0]+int(orbit_r*np.cos(np.deg2rad(phi)))
    y_orbit=Centerloc[1]+int(orbit_r*np.sin(np.deg2rad(phi)))
    #print(f"x:{x_orbit} y:{y_orbit} phi:{int(orbitphi)}")
    frame= cv2.circle(frame,(x_orbit,y_orbit),size_r, color, -1)
    return frame

ORBITAL_RSIZE=3
ORBITAL_PHI=0
ORBITAL_DPHI=1 #0.5deg delta
dr=(SUN_RSIZE+ORBITAL_R) #*(orbitdphi) #*np.pi/180)
orbitloc=(SUN_LOC[0],SUN_LOC[1]+SUN_RSIZE+ORBITAL_R)
satsn=0


#2021/05/06 Window priority
print(cv2.WND_PROP_FULLSCREEN)
cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Frame",cv2.WND_PROP_FULLSCREEN,0)


Start_Time=datetime.datetime.today()
Delta_T=60
#Sat_Time_Space=Delta(minutes=1)
Sat_Time_Space=Delta(seconds=Delta_T)
Sat_dic={}
Poff=180
Roff=0
#mins=time.minute

while True:
    _, frame = cap.read()
    frame_time=datetime.datetime.today()
    if frame_time >= Sat_Time_Space+Start_Time:
        Start_Time=frame_time 
        dr=(SUN_RSIZE+ORBITAL_R)
        Sat_dic[satsn]={"Time":Start_Time,"Phi_Offset":Poff,"Sat_Radius":dr}
        print("New Sat added")
        print(Sat_dic[satsn])
        Poff-=30
        satsn+=1

        if Poff <=-180:
            Poff=180
            ORBITAL_R+=5

        print(frame_time)



    #frame = cv2.resize(frame,(h,w))
    
    if(frame is None):
            continue
    
    frame = cv2.circle(frame,SUN_LOC,SUN_RSIZE, (0,0,250), -1)
    #Satn to frame 
   # frame=cv2.putText(frame,str(satsn),(SUN_LOC[0]-15,SUN_LOC[1]+15),
    #    cv2.FONT_HERSHEY_PLAIN,3,(255,255,255))
    
    if satsn:

        for n,sat in Sat_dic.items():
            frame=Orbiral(frame,SUN_LOC,sat["Sat_Radius"],ORBITAL_RSIZE,ORBITAL_PHI-sat["Phi_Offset"],(0,0,255))
    
        #for offphi in range(-180,180,satsn):
            #if n==satsn:
              #  for R_OFF, fadeSeconds in zip(np.linspace(ORBITAL_RSIZE,1,ORBITAL_RSIZE),np.linspace(0,Delta//2,int(ORBITAL_RSIZE))):
                    
               #     if frame_time >= Sat_Time_Space+fadeSeconds:
                #        print("Fade:",R_OFF)
                  #      frame=Orbiral(frame,SUN_LOC,sat["Sat_Radius"],ORBITAL_RSIZE-int(R_OFF),ORBITAL_PHI-sat["Phi_Offset"],(255,0,255))
                  #  else:
                        #frame=Orbiral(frame,SUN_LOC,sat["Sat_Radius"],ORBITAL_RSIZE,ORBITAL_PHI-sat["Phi_Offset"],(0,0,255))
    
    ORBITAL_PHI+=ORBITAL_DPHI
    if ORBITAL_PHI>=360:
        ORBITAL_PHI=0

    #Line 
    #img = cv2.line(frame,logoloc,orbitloc,(255,0,0),5)
    
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# VideoCaptureオブジェクト破棄
cap.release()
cv2.destroyAllWindows()    


