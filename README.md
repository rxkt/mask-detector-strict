Dataset obtained from  
https://www.kaggle.com/prithwirajmitra/covid-face-mask-detection-dataset/notebooks

The data folder with all images used was added to this repository to show the outcome of preprocessing the data using `face_crop.py`.  
This achieves a 97~98% training accuracy, 93% test accuracy with our CNN model as opposed to a low 90% training accuracy, and an even lower test accuracy.

To-do:

- Currently overfitting with 80% validation accuracy due to very low number of input files after preprocessing. Currently this dataset is a poor representation of how a picture of a face would be. Will add more images to train later.
- Adding a "nose", "mouth" detection using dlib or opencv after we determine that a mask is in the picture. We want to be able to determine if this person is not "fully" or "properly" wearing a mask.

Dependencies:  
Image  
opencv-python  
tensorflow  
keras
