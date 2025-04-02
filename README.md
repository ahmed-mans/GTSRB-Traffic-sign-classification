# Traffic Sign Image classification - 94% Accuracy

## Project Summary
This project shows how to train a simple CNN model from scratch to classify traffic signs images into 43 different classes:<br>
{0:'20 km/h', 1:'30 km/h', 2:'50 km/h', ... , 42:' End of the overtaking restriction'}

The notebook 'gtsrb_classification.ipynb' was used to implement and train the CNN for the classification task.

# Version
Python version : *3.10.12*
Tensorflow version : *2.17.1*

## Dataset Description
The dataset consists of __51 839__ images spread accross __43__ traffic sign classes, for which 39 209 images are for training set and 12 630 images are for the test set. 
The following image shows sample for some classes from the training set as well as the respective number of images for each classes in brackets.

![image](https://github.com/user-attachments/assets/3be5b7b1-6169-45fb-ba33-4367ae99e7e0)

### Note:
- One can see that class imabalance is present in the dataset. For instance, class 0 representing the traffic sign '20 km/h' has 210 images compared to class 1 for traffic sign '30 km/h' having over 2000 images.
  

You can download the GTSRB dataset [here](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign).


# Code
The CNN model can be found in the **get_model_from_scratch.py**  file.

The entire notebook can be found the **gtsrb_classification.ipynb** file. This notebook is compatible with Kaggle only.

# Test with new branch

# Reference
https://www.kaggle.com/code/yacharki/traffic-signs-image-classification-97-cnn
