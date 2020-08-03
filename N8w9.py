#Tech-Gym-13-16-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^

###�n�C�p�[�p�����[�^###
#�������֐�
#�B��w�̐��A�B��w�̃`�����l����
#�h���b�v�A�E�g���銄���irate�j
#�w�K���iIr�j
#�œK���֐��ioptimizer�j��
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

#�œK���֐���ς��āA���𗦂̕ω��𒲂ׂ�
OPT_list = ["sgd","adadelta","adam","adamax","nadam"]
OPT_color = {"sgd":"blue","adadelta":"red","adam":"orange","adamax":"green","nadam":"black"}

#�O���t�`��p�̋󃊃X�g
acc = []

for OPT in OPT_list:    
    #���f���̐���
    model.compile(optimizer=OPT, loss="categorical_crossentropy", metrics=["accuracy"])
    
    #�w�K
    history = model.fit(X_train, y_train, verbose=0, epochs=10)

    #���f���]��
    score = model.evaluate(X_test, y_test, verbose=0)
    
    #�K�v�ł���Ε\��
    #print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))
    acc.append(score[1])

    #acc�Aval_acc�̃v���b�g
    plt.plot(history.history["acc"], label="acc_"+OPT, ls="-", marker="o", color=OPT_color[OPT])
    plt.ylabel("accuracy")
    plt.xlabel("epoch")
    plt.legend(loc="best")
    plt.show()
