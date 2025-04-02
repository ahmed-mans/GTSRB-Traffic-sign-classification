# Traffic Sign Image classification - 94% Accuracy

## Project Summary
This project shows how to train a simple CNN model from scratch to classify traffic signs images into 43 different classes:<br>
{0:`20 km/h`, 1:`30 km/h`, 2:`50 km/h`, ... , 42:`End of the overtaking restriction`}

The notebook `gtsrb_classification.ipynb` was used to implement and train the CNN for the classification task.

# Version
Python version : *3.10.12*
Tensorflow version : *2.17.1*

## Dataset Description
The dataset consists of __51 839__ images spread accross __43__ traffic sign classes, for which 39 209 images are for training set and 12 630 images are for the test set. 
The following image shows sample for some classes from the training set as well as the respective number of images for each classes in brackets.

![image](https://github.com/user-attachments/assets/3be5b7b1-6169-45fb-ba33-4367ae99e7e0)

For training the CNN model, the training set was split into a training and validation set using in a 80-20 ratio.
### Note:
- One can see that class imabalance is present in the dataset. For instance, class 0 representing the traffic sign `20 km/h` has __210__ images compared to class 1 for traffic sign `30 km/h` having over __2000__ images.
- The dataset can be downloaded [here](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign).


# CNN Model Architecture

The model architecture consists of two sets of two consecutive CNN layers with activation and pooling layers.
These two sets are then followed by 4 fully connected layers ending a fifth layer outputing the softmax probabilities for each of the 43 classes of the dataset.
The model implementation in python can be found in the `get_model_from_scratch.py` file.

# Hyper Parameters

- Epochs: __20__
- Optimizer: __Adam__
- Initial Learning Rate: __0.001__
- Batch size: __64__

# Accuracy on Test Set
The model, once trained with the configuration mentioned above, outputs an accuracy of __94%__ on the test set.
![image](https://github.com/user-attachments/assets/993e7d6b-b223-4a34-8ffb-53ad40758280)

# Reference
https://www.kaggle.com/code/yacharki/traffic-signs-image-classification-97-cnn
