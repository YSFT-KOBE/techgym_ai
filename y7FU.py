#Tech-Gym-13-21-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�摜����

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

# �J�e�S���̎w��
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

# �摜�T�C�Y���w��
image_w = 64 
image_h = 64

# �f�[�^�����[�h

# �f�[�^�𐳋K������


# ���f�����\�z 


model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# ���f�����P������


# ���f����]������

