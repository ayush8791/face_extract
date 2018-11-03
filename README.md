# face_extract
extract faces of an image with 90+ accuracy (profile faces)
#  Dlib is an Awesome Library for image and video processing using deep learning in background
I have used following libraries:
1. os
2. dlib
3. opencv

# Selection of an Model
Although dlib provides many options I have opted for CNN based detector as this model can detect faces at different angles as well which is way better choice than HOG detector.

Python provides os library by default although you can install other required library using pip
dlib is an C++ library therefore requires you to install Cython and CMake as well in order to work properly.
start by installing :
1. Cython
2. CMake
3. dlib
4. opencv

After installing above libraries you are good to go!
Note: the images should be in same working directory as that of the execution. 



