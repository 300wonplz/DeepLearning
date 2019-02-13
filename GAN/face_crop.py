import cv2
import os

path = '../../datasets/celebA/img_align_celeba/img_align_celeba/'
face_cascade = cv2.CascadeClassifier('../../haarcascade/haarcascade_frontalface_default.xml')
size = 100
imgNum  = 0


file_name = os.listdir(path)
    
for file in file_name[0:5000]: 
    img = cv2.imread(path + file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    
    for (x,y,w,h) in faces:
        cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
        # 이미지를 저장
        cv2.imwrite("../../datasets/celebA/img_align_celeba/cropped/"+str(imgNum) + ".jpg", cropped)
        imgNum += 1

print('종료')