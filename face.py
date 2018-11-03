
import cv2
import dlib
import os
#import face_recognition

# File name to be processed 
file_name = "cl.jpg"

# Create a CNN Face detector from dlib
cnn_face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

# Load the image into an array
image = cv2.imread(file_name)

# Run the CNN face detector on the image data.
# The result will be the bounding boxes of the faces in our image.
detected_faces = cnn_face_detector(image, 1)

# Number of faces found within the image
print("I found {} faces in the file {}".format(len(detected_faces), file_name))


# Create a directory "faces" such that faces will be cropped and stored with names as count
count=0
path=os.getcwd()
os.mkdir(path+"\\faces")
os.chdir(path+"\\faces")
# Loop through each face we found in the image
for face in detected_faces:
    x=face.rect.left()
    y=face.rect.top()
    w=face.rect.right()-x
    h=face.rect.bottom()-y
    cv2.rectangle(image,(x,y),(w+x,h+y),(0,0,255),2)
    count+=1
    cv2.imwrite(str(count)+".jpg",image[y:y+h,x:x+h])
	        
# Apart from cropping faces and storing we will also produce an final result image depicting faces detected with rectangular boxes

os.chdir(path)
cv2.imwrite("result.jpg",image)
