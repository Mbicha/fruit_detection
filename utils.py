import cv2
import numpy as np
from keras.models import load_model

model = load_model('fruits_classfication_20epochs.h5')

def classify_fruit(img_path: str, img_size: int) -> str:
    """
    Parameters
    ----------
    img_path - Image path
    img_size - size of an image
    ------
    Return
    ------
    return string
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    resize_image = cv2.resize(img, (img_size, img_size))
    img_array = np.array(resize_image) / 255
    arr_reshaped = img_array.reshape(-1, img_size, img_size, 3)

    labels = ['orange', 'banana', 'mixed', 'apple']
    predict = np.argmax(model.predict(arr_reshaped), axis=-1)
    for i in predict:
        if labels[i] in labels:
            return labels[i]
        else:
            return f"No Match"
