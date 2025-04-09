# Traffic Sign Image classification - 94% Accuracy

## 🚦 Project Overview
This project demonstrates how to train a __Convolutional Neural Network (CNN)__ from scratch to classify traffic sign images into __43 distinct categories__.
Each class represents a specific traffic sign, such as:
```
0: 20 km/h,  
1: 30 km/h,  
2: 50 km/h,  
...  
42: End of the overtaking restriction
```

### 🧪 Implementation

The full training and implementation process is contained in the notebook `traffic_sign_classification.ipynb`.

It includes:
- Dataset preprocessing
- Custom CNN architecture<br>
- Training and evaluation of the model

## 🗂️ Dataset Description
The dataset contains a total of __51,83 images__ categorized into __43 traffic sign classes__.

It is divided into:
- __Training set__: 39,209 images
- __Test set__: 12,630 images

The image below showcases a few sample classes from the training set, along with the __number of images per class__ indicated in brackets.

To train the CNN model effectively, the original training set was divided into two subsets:

- __80%__ for training<br>
- __20%__ for validation.
  
![image](https://github.com/user-attachments/assets/3be5b7b1-6169-45fb-ba33-4367ae99e7e0)


### Notes

- **Class imbalance** is present in the dataset. For example:  
  - **Class 0** (`20 km/h`) has only **210 images**  
  - **Class 1** (`30 km/h`) has over **2,000 images**

  This imbalance can affect model performance and may require techniques like **class weighting** or **data augmentation** to mitigate it.

- 📥 **Dataset Download**:  
  [GTSRB - German Traffic Sign Dataset on Kaggle](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)


## 🧠 CNN Model Architecture

This project features a **custom-built Convolutional Neural Network (CNN)** tailored for traffic sign classification.

- The architecture includes **two convolutional blocks**, each consisting of:
  - Two consecutive `Conv2D` layers with activation functions  
  - Followed by `MaxPooling` layers for downsampling

- The extracted features are then passed through **four fully connected (Dense) layers**, ending with a **final output layer** using `softmax` activation to produce class probabilities across the **43 traffic sign classes**.

📄 **Model Implementation**:  
[`get_model_from_scratch.py`](get_model_from_scratch.py)

## ⚙️ Training HyperParameters

- Epochs: __20__
- Optimizer: __Adam__
- Initial Learning Rate: __0.001__
- Batch size: __64__

## 📉 Model Training Progress

The following graphs illustrate the evolution of the model's **accuracy** and **loss** throughout the training process. As shown, the model reached convergence after **9 epochs**.

![traffic sign classification graphs](https://github.com/user-attachments/assets/c6401608-5424-45ce-ae7f-244dfaa9fe51)

## 📤 Inference on the test set
The visualization below displays the inference results on a selection of 20 test set images. For each image, both the true label and the predicted class are shown to assess the model's performance on unseen data.

![traffic sign classification inference test set](https://github.com/user-attachments/assets/b4fb7c94-c799-49f0-a488-d9631c6da2c5)

## ✅ Test Set Accuracy

After training the model with the specified configuration, it achieved an accuracy of **94%** on the test set, showcasing its high performance and ability to classify traffic signs effectively.

![Test Set Accuracy](https://github.com/user-attachments/assets/993e7d6b-b223-4a34-8ffb-53ad40758280)

## Reference
https://www.kaggle.com/code/yacharki/traffic-signs-image-classification-97-cnn
