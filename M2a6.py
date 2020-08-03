#Tech-Gym-13-12-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^

#�K�v�ȃ��C�u����
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline

#keras
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Activation

#���\�]��
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#MNIST�f�[�^
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#�s��̑傫�����m�F
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  

#�͂��߂�6000��1�����s��̌`�ɕύX
X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

#�s��̑傫�����m�F
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)    

#���f���̃C���X�^���X���쐬
model = Sequential()

# ���̓��j�b�g����784�A1�ڂ̑S�����w�̏o�̓��j�b�g����256
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))

# 2�ڂ̑S�����w�̏o�̓��j�b�g����128
model.add(Dense(128))
model.add(Activation("relu"))

# 3�ڂ̑S�����w�i�o�͑w�j�̏o�̓��j�b�g����10
model.add(Dense(10))
model.add(Activation("softmax"))

#���f���̐���
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

#�w�K
history = model.fit(X_train, y_train, verbose=0, epochs=10)

#acc�Aval_acc�̃v���b�g
plt.plot(history.history["acc"], label="acc", ls="-", marker="o")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.show()

#���f���\��
model.summary()

#���f���]��
score = model.evaluate(X_test, y_test, verbose=1)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#�����s��
print('Cross tabulation')
y_pred = model.predict_classes(X_test)
y_test_c = np.argmax(y_test, axis=1)

#���\�]��
print(confusion_matrix(y_pred, y_test_c))
print('����:{:.3f}'.format(accuracy_score(y_pred, y_test_c)))


