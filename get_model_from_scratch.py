def get_model_from_scratch(num_classes, input_shape):

    #Dropout percentage
    dp_value = 0.1

    # Kernel size for convolutional layers
    kernel_size = 7
    
    inputs = Input(shape=input_shape)

    # Normalizing the data
    x = Rescaling(1./255)(inputs)

    # First set of 2 consecutive conv. layers + activation + pooling
    x = Conv2D(8, kernel_size, padding='valid')(x) 
    x = Conv2D(16, kernel_size, padding='valid')(x)
    x = Activation('relu')(x) 
    x = MaxPooling2D()(x)    

    # Second set of 2 consecutive conv. layers + activation + pooling
    x = Conv2D(32, kernel_size, padding='valid')(x)
    x = Conv2D(64, kernel_size, padding='valid')(x)
    x = Activation('relu')(x) 
    x = MaxPooling2D()(x)   
    
    # Flatten the feature maps
    flattened = Flatten()(x) 

    # Fully connected layers
    x = Dense(480, activation='relu')(flattened)           
    x = Dropout(dp_value)(x)
    x = Dense(240, activation='relu')(x)
    x = Dropout(dp_value)(x)
    x = Dense(120, activation='relu')(x)
    x = Dropout(dp_value)(x)
    x = Dense(84, activation='relu')(x)  
    x = Dropout(dp_value)(x)
    
    # Softmax output layer
    headout = Dense(num_classes, activation="softmax")(x)  
    
    # Create model
    model = Model(inputs=inputs, outputs=headout, name='Model_1')
    
    return model
