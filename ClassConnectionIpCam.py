import urllib
import numpy as np
import cv2

class classConnectionAndCapturedipcam():
   
   #conexion con camara
    def connection(url):
        imgResp= urllib.urlopen(url)

        return imgResp
    #Funcion de captura de imagenes
    def capturedImage(imgResp):
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        
        img=cv2.imdecode(imgNp,-1)
        return img
    #Visualización de imagenes con opncv
    def streamVideo(img):
        cv2.imshow('video', img)

    #Funcion que crea carpeta conetenedora
    def make_folder(path_folder):

        if not os.path.exists(path_folder):
            os.makedirs(path_folder

    #funcion que guarda la imagen dentro de una ruta 
    def save_images_in_path(path_folder,image):
        imageio.imwrite(path_folder,image)

