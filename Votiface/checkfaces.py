from fileinput import filename
import cv2
import numpy as np
import face_recognition
import os
import shutil


#with the assumption that the images of all the citizens are in this folder
src_path = 'imageBasic'
dest_path = 'VotedPeople'
images = []
classNames = []
#myList = os.listdir(src_path)
#print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{src_path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)

def compare(faceDistance):
    if faceDistance > 0.45:  #reduce this value if you want to increase accuracy
        return False
    else:
        return True

image1= cv2.imread('imageBasic/isha.jpg')   #image1 is the variable storing the first image
image2 = cv2.imread('imageBasic/rupak.jpg')  #image2 is the variable storing the second image



def findEncoding(image): #returns 128-d encoding of the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(image)[0]
    return encode

firstphoto= findEncoding(image1)
secondphoto = findEncoding(image2) 


def comparison(firstphoto,secondphoto): #compares the two images and returns the bool result
    faceDistance = face_recognition.face_distance([firstphoto],secondphoto)
    results = compare(faceDistance)
    return results

print(comparison(firstphoto,secondphoto))

    

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

# encodeListKnown = findEncodings(images)
# print('Encoding Complete')

# def votedClassifier(VotedPerson):
#     for file_name in classNames:
#         if file_name.upper() == VotedPerson:
#             #print('I am where you want')
#             #os.path.splitext(cl)[0])
#             file_name = file_name + '.jpg'
#             shutil.move(os.path.join(src_path, file_name), dest_path)
    
 
# cap = cv2.VideoCapture(0)
# def comparison():
#     matches = face_recognition.compare_faces(encodeListKnown,encodeFace, tolerance=0.5)

# while True:
#     success, img = cap.read()
#     #print(f'wow {success}ful people')
#     imgS = cv2.resize(img,(0,0),None,0.25,0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
#     for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown,encodeFace, tolerance=0.5)
#         faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
#         #matches = compare(faceDis)
#         print(f'matches is {matches}')
#         matchIndex = np.argmin(faceDis)
        

#         if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
#             #print(name)
#             y1,x2,y2,x1 = faceLoc
#             y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
#             cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#             cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#             cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

        
#             print(f'{name} is in the frame')
#             votedClassifier(name)
#             exit()
        
          

#     cv2.imshow('Webcam',img)
#     cv2.waitKey(1)

    








