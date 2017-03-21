#_*_ coding: UTF-8 _*_

from math import sqrt
import numpy as np
import cv2

'''
    Teste de reconhecimento de elementos da face e a comparação entre eles.
'''
face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_mcs_mouth.xml')

def detectarElementos(gray,cascade):
   return cascade.detectMultiScale(gray,1.3,10)

def marcarFace(img,gray,color,cascade):
    elementos = detectarElementos(gray,cascade)
    for (x,y,w,h) in elementos:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        yield roi_gray,roi_color

def marcarElementos(img, gray, color, cascade,):
    elementos = detectarElementos(gray,cascade)
    for (x, y, w, h) in elementos:
        cv2.rectangle(img, (x, y), (x + w, y + h),color, 2)
        gray[y:y +h, x:x + w] = 0
        yield (x+w/2,y+h/2)

def calcularDistancia(middle,lista_distancia,img):
    for middle_element1 in middle:
       for middle_element2 in middle:
           if (middle_element1 != middle_element2):
               cv2.line(img, middle_element1, middle_element2, (255, 255, 255), 2)
               lista_distancia.append(sqrt((middle_element1[0] - middle_element2[0])** 2 + ((middle_element1[1] - middle_element2[1])** 2)))
           else:
               break


img = cv2.imread('Carly.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
middle = []
lista_distancia = []

for (roi_gray,roi_color) in marcarFace(img,gray,(255,0,0),face_cascade):
    for middle_element in marcarElementos(roi_color,roi_gray,(0,255,0),eye_cascade):
        middle.append(middle_element)  
    for middle_element in marcarElementos(roi_color,roi_gray,(0,0,255),nose_cascade):
        middle.append(middle_element)
    for middle_element in marcarElementos(roi_color,roi_gray,(0,0,0),mouth_cascade):
        middle.append(middle_element)
    calcularDistancia(middle,lista_distancia,roi_color)

print(middle) 
print(lista_distancia)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()