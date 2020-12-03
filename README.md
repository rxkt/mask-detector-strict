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

- Adding a "nose", "mouth" detection using dlib or opencv after we determine that a mask is in the picture. We want to be able to determine if this person is not "fully" or "properly" wearing a mask.

Dependencies:  
Image  
opencv-python  
tensorflow  
keras
