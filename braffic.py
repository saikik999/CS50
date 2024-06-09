import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

def load_data(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        path = os.path.join(data_dir, label)
        if os.path.isdir(path):
            for img_file in os.listdir(path):
                img_path = os.path.join(path, img_file)
                image = plt.imread(img_path)
                images.append(image)
                labels.append(int(label))
    return np.array(images), np.array(labels)

data_dir = 'gtsrb'
images, labels = load_data(data_dir)

images = images / 255.0

num_classes = len(np.unique(labels))
labels = to_categorical(labels, num_classes)

x_train, x_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val), batch_size=32)

val_loss, val_acc = model.evaluate(x_val, y_val)
print(f'Validation accuracy: {val_acc:.2f}')

def predict_traffic_sign(image_path):
    image = plt.imread(image_path)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)
    return predicted_class

predicted_class = predict_traffic_sign('test_image.png')
print(f'Predicted traffic sign class: {predicted_class[0]}')