Dataset initially obtained from  
https://www.kaggle.com/prithwirajmitra/covid-face-mask-detection-dataset/notebooks  
and later compiled with data from  
https://www.kaggle.com/omkargurav/face-mask-dataset

The sample-data folder with images used was added to this repository to show the outcome of preprocessing the data using `face_crop.py`. The actual data folder is not being tracked nor added to this repo because it will be updated with more images.

Training Accuracy: ~98.5%  
Validation Accuracy: ~97.5%  
Test Accuracy: 95%

To-do:

~~- Currently overfitting with 80% validation accuracy due to very low number of input files after preprocessing. Currently this dataset is a poor representation of how a picture of a face would be. Will add more images to train later.~~

~~- Adding a "nose", "mouth" detection using dlib or opencv after we determine that a mask is in the picture. We want to be able to determine if this person is not "fully" or "properly" wearing a mask.~~

~~- Integration of the mask model & the dlib mouth/mask detection function~~

- Add a code pipeline if I want to host this eventually?

Ideally we would be able to train a model of an "improper mask" vs. a "proper mask" but there is not yet a dataset out there at the moment.  
OpenCV Mouth/Nose haarcascades were too unreliable as they detected eyes as mouths/noses, so dlib was used instead.

Dependencies:  
Image  
opencv-python  
tensorflow  
keras  
dlib  
imutils
