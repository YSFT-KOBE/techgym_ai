#Tech-Gym-13-19-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^:���f���ۑ�

import keras
from sklearn import datasets
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical

# �A�����̃T���v���f�[�^��ǂݍ���
iris = datasets.load_iris()
in_size = 4
nb_classes=3

# ���x���f�[�^��one-hot�x�N�g���ɒ���
x = iris.data
y = to_categorical(iris.target, nb_classes)

# ���f�����`
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))

# �R���p�C��
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# �w�K�����s
model.fit(x, y, batch_size=20, epochs=50)

# ���f����ۑ�
model.save('iris_model.h5')

# �w�K�ςݏd�݃f�[�^��ۑ�
model.save_weights('iris_weight.h5')

# �A�����̃T���v���f�[�^��ǂݍ���
iris = datasets.load_iris()
in_size = 4
nb_classes=3

# ���x���f�[�^��one-hot�x�N�g���ɒ���
x = iris.data
y = to_categorical(iris.target, nb_classes)

# ���f����Ǎ�
model = load_model('iris_model.h5')

# �d�݃f�[�^��Ǎ�
model.load_weights('iris_weight.h5')

# ���f����]��
score = model.evaluate(x, y, verbose=1)
print("����=", score[1])


