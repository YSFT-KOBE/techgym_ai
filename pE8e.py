#Tech-Gym-13-12-Q
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

#�s��̑傫�����m�F

#���f���̃C���X�^���X���쐬

# ���̓��j�b�g����784�A1�ڂ̑S�����w�̏o�̓��j�b�g����256

# 2�ڂ̑S�����w�̏o�̓��j�b�g����128

# 3�ڂ̑S�����w�i�o�͑w�j�̏o�̓��j�b�g����10

#���f���̐���

#�w�K

#acc�Aval_acc�̃v���b�g

#���f���\��

#���f���]��

#�����s��


#���\�]��



