#Tech-Gym-13-13-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^

###�n�C�p�[�p�����[�^###
#�������֐�
#�B��w�̐��A�B��w�̃`�����l����
#�h���b�v�A�E�g���銄���irate�j
#�w�K���iIr�j��
#�œK���֐��ioptimizer�j
#�덷�֐��iloss�j
#�o�b�`�T�C�Y�ibatch_size�j
#�G�|�b�N���iepochs�j

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
from keras import optimizers

#���\�]��
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#MNIST�f�[�^
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#�s��̑傫�����m�F
#print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  

#�͂��߂�6000��1�����s��̌`�ɕύX
X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

#�s��̑傫�����m�F
#print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)    

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

#�w�K����ς��āA���𗦂̕ω��𒲂ׂ�
SGD_list = [0.001,0.01,0.1,1,10,100,1000,10000,100000]

#�O���t�`��p�̋󃊃X�g
acc = []

for LR in SGD_list:
    #�w�K��
    sgd = optimizers.SGD(lr=LR)
    
    #���f���̐���
    model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])
    
    #�w�K
    history = model.fit(X_train, y_train, verbose=0, epochs=3)

    #���f���]��
    score = model.evaluate(X_test, y_test, verbose=0)
    acc.append(score[1])

#�O���t������
fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.set_title("Parameter:LR")
ax.set_xlabel("LR")
ax.set_ylabel("acc")
ax.semilogx(SGD_list, acc, label="acc")
ax.legend()
ax.plot()
plt.show()


