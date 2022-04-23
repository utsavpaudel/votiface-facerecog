import cv2
import numpy as np
import face_recognition

def compare(faceDistance):
    if faceDistance > 0.5:
        return False
    else:
        return True

#changing color to RGB for train image
imgUtsav = face_recognition.load_image_file('imageBasic/SantoshK.jpg')
imgUtsav = cv2.cvtColor(imgUtsav,cv2.COLOR_BGR2RGB)

#changing color to RGB for test image
imgTest = face_recognition.load_image_file('imageBasic/isha.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgUtsav)[0]
encodeUtsav = face_recognition.face_encodings(imgUtsav)[0]
cv2.rectangle(imgUtsav,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,200,0),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,200,0),2)

#print(faceLoc)


faceDistance = face_recognition.face_distance([encodeUtsav],encodeTest)

#results = face_recognition.compare_faces([encodeUtsav],encodeTest)
results= compare(faceDistance)



print(results,faceDistance)
print(round(faceDistance[0],2))

if results == False:
    #print('milena')
    cv2.putText(imgTest, f'{results}{round(faceDistance[0],2)}:Milne orne kei haina rachha, natak',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

else:
    #print('milyo')
    cv2.putText(imgTest, f'{results}{round(faceDistance[0],2)} Ustai la ustai',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,25),2)


#print(results)

cv2.imshow('Utsav Paudel', imgUtsav)
cv2.imshow('Utsav Test', imgTest)
cv2.waitKey(0)




