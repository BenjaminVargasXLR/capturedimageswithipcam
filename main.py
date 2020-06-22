import ClassConnectionIpCam as cip

def __main__():

    #peticion de url de la camara
    url = input("Ingrese url de camara:")
    #conexion a camara
    imgresp = cip.classConnectionAndCapturedipcam.connection(url)
    #definicion de capeta contenedora de imagenes
    pathfolder = "C:\pathimages"
    #creacion de carpte contenedora
    cip.classConnectionAndCapturedipcam.make_folder(path_folder)

    while True:
        #captura de imagen
        img = cip.classConnectionAndCapturedipcam.capturedImage(imgresp)
        #Guardado de imagenes en path
        cip.classConnectionAndCapturedipcam.save_images_in_path(path_folder,img)
        #stream de imagenes con opencv
        cip.classConnectionAndCapturedipcam.streamVideo(img)










