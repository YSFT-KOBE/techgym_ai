#Tech-Gym-13-19-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^:���f���ۑ�

import keras
from sklearn import datasets
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical


# ���x���f�[�^��one-hot�x�N�g���ɒ���
x = iris.data
y = to_categorical(iris.target, nb_classes)

# ���f�����`


# �R���p�C��
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# �w�K�����s


# ���f����ۑ�


# �w�K�ςݏd�݃f�[�^��ۑ�

# �A�����̃T���v���f�[�^��ǂݍ���


# ���x���f�[�^��one-hot�x�N�g���ɒ���
x = iris.data
y = to_categorical(iris.target, nb_classes)

# ���f����Ǎ�


# �d�݃f�[�^��Ǎ�


# ���f����]��
score = model.evaluate(x, y, verbose=1)
print("����=", score[1])



