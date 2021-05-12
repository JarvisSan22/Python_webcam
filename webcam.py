import numpy as np
import cv2 
import math
h=300
w=300
cap = cv2.VideoCapture(0)
SUN_LOC=(200,40)
SUN_RSIZE=15
ORBITAL_R=10



def Orbiral(frame,Centerloc,orbit_r,size_r,phi,color):
    x_orbit=Centerloc[0]+int(orbit_r*np.cos(np.deg2rad(phi)))
    y_orbit=Centerloc[1]+int(orbit_r*np.sin(np.deg2rad(phi)))
    #print(f"x:{x_orbit} y:{y_orbit} phi:{int(orbitphi)}")
    frame= cv2.circle(frame,(x_orbit,y_orbit),size_r, color, -1)
    return frame

ORBITAL_RSIZE=2

ORBITAL_PHI=0
ORBITAL_DPHI=1 #0.5deg delta


#2021/05/06 Window priority
print(cv2.WND_PROP_FULLSCREEN)
cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Frame",cv2.WND_PROP_FULLSCREEN,0)

dr=(SUN_RSIZE+ORBITAL_R) #*(orbitdphi) #*np.pi/180)
orbitloc=(SUN_LOC[0],SUN_LOC[1]+SUN_RSIZE+ORBITAL_R)
while True:
    _, frame = cap.read()
    #frame = cv2.resize(frame,(h,w))
    
    if(frame is None):
            continue
    
    frame = cv2.circle(frame,SUN_LOC,SUN_RSIZE, (0,0,250), -1)

    x_orbit=SUN_LOC[0]+int(dr*np.cos(np.deg2rad(ORBITAL_PHI)))
    y_orbit=SUN_LOC[1]+int(dr*np.sin(np.deg2rad(ORBITAL_PHI)))
    #print(f"x:{x_orbit} y:{y_orbit} phi:{int(orbitphi)}")
    for offphi in range(-180,180,30):
        frame=Orbiral(frame,SUN_LOC,dr,ORBITAL_RSIZE,ORBITAL_PHI-offphi,(0,255,255))
    #frame=Orbiral(frame,SUN_LOC,dr,ORBITAL_RSIZE,ORBITAL_PHI-180,(0,255,0))
    #frame= cv2.circle(frame,(x_orbit,y_orbit),ORBITAL_RSIZE, (0,255,0), -1)
    #frame= cv2.circle(frame,(x_orbit,y_orbit),ORBITAL_RSIZE, (255,0,0), -1)
    orbitloc=(x_orbit,y_orbit)
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


