import numpy as np
import cv2 
import math
h=300
w=300
cap = cv2.VideoCapture(0)
SUN_LOC=(40,40)
SUN_RSIZE=30
ORBITAL_R=5

ORBITAL_RSIZE=2

ORBITAL_PHI=0
ORBITAL_DPHI=1 #0.5deg delta


#Model loc 
cascade="haarcascade_frontalface_extended" #haarcascade_upperbody
cascade_path = f"D:/Python_scripts/Python_video_edit/Webcam/opencv/data/haarcascades/haarcascade_frontalface_extended.xml"
cascade_path = f"D:\Python_scripts\Python_video_edit\Webcam\opencv\data\haarcascades\haarcascade_frontalcatface_extended.xml"
cascade_path = f"D:\Python_scripts\Python_video_edit\Webcam\opencv\data\haarcascades\haarcascade_upperbody.xml"
cascade_path = f"D:\Python_scripts\Python_video_edit\Webcam\opencv\data\haarcascades\haarcascade_frontalface_default.xml"

cascade = cv2.CascadeClassifier(cascade_path)
print(cascade )
dr=(SUN_RSIZE+ORBITAL_R) #*(orbitdphi) #*np.pi/180)
orbitloc=(SUN_LOC[0],SUN_LOC[1]+SUN_RSIZE+ORBITAL_R)


while True:
    _, frame = cap.read()
    #fh,fw,c=frame.shape
   # ratio=fh//fw
    
    if(frame is None):
            continue

    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #物体確認
    facerect = cascade.detectMultiScale(frame_gray, 1.4,5)
    #print(facerect)
    color = (255, 255, 255) #白
    #検出した場合
    #print(len(facerect))
    if len(facerect) > 0:

         #検出した顔を囲む矩形の作成
        for rect in facerect:
            cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# VideoCaptureオブジェクト破棄
cap.release()
cv2.destroyAllWindows()    


