#Tech-Gym-13-17-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^

#�K�v�ȃ��C�u����
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#MNIST�f�[�^
from keras.datasets import mnist

#keras
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical
from keras.utils.vis_utils import plot_model

#���\�]��
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# �f�[�^�����[�h���܂�
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# �����ł͑S�f�[�^�̂����A�w�K�ɂ�6000�A�e�X�g�ɂ�1000�̃f�[�^���g�p����
X_train = X_train[:6000].reshape(-1, 28, 28, 1)
X_test = X_test[:1000].reshape(-1, 28, 28, 1)
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

# ���f�����`���܂�
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),input_shape=(28,28,1)))
model.add(Activation('relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(X_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(X_test, y_test))

#���f���]��
score = model.evaluate(X_test, y_test, verbose=1)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

###�K�v�Ȃ�ȉ���\������####
#�����s��
#print('Cross tabulation')
#y_pred = model.predict_classes(X_test)
#y_test_c = np.argmax(y_test, axis=1)

#���\�]��
#print(confusion_matrix(y_pred, y_test_c))
#print('����:{:.3f}'.format(accuracy_score(y_pred, y_test_c)))

#���f���\��
model.summary()

#���f���̏d��
print(model.weights)

# ���C���[���Ƃ̃p�����[�^���擾�ł���
# list of the layers
# �w�̔z��̔ԍ����킩��
for i, l in enumerate(model.layers):
    print(i, l)

# ���C���[��weights��bias
w1 = model.layers[0].get_weights()[0] 
b1 = model.layers[0].get_weights()[1]

w2 = model.layers[2].get_weights()[0] 
b2 = model.layers[2].get_weights()[1] 

w7 = model.layers[7].get_weights()[0]
b7 = model.layers[7].get_weights()[1]

w10 = model.layers[10].get_weights()[0]
b10 = model.layers[10].get_weights()[1]

#�p�����[�^�̑傫��
print(w1.shape, b1.shape)
print(w2.shape, b2.shape)
print(w7.shape, b7.shape)
print(w10.shape, b10.shape)

#�p�����[�^�ƃo�C�A�X
print(w1, b1)
