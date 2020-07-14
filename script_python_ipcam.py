import cv2
import os

import time

path = 'C:/Users/usuario/Desktop/ToolOrientation/deteccionfrontal/realImagesCCTV'





#Funcion que crea carpeta conetenedora
def make_folder(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)



captura = cv2.VideoCapture('rtsp://192.168.1.10:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream')
make_folder(path)
count=0
while True:



 
  check,img= captura.read()
  
 # cv2.namedWindow("main", cv2.WINDOW_NORMAL)
 # cv2.imshow('main',img)

  cv2.imwrite(path+'/frame%d.jpg'%count,img)
  count +=1


  #time.sleep(1)
  print("Frame capturado")

captura.release()
cv2.destroyAllWindows()
