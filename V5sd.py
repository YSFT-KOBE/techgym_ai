#Tech-Gym-13-24-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�ړ]�w�K:VGG16

#�K�v�Ȃ��̂��C���|�[�g
import os
import json
import numpy as np
import urllib.request
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image

#�摜��\�����邽�߂ɃC���|�[�g
import matplotlib.pyplot as plt
%matplotlib inline

def download_json():
    url = "https://gist.githubusercontent.com/PonDad/4dcb4b242b9358e524b4ddecbee385e9/raw/dda9454f74aa4fafee991ca8b848c9ab6ae0e732/imagenet_class_index.json"
    title = "imagenet_class_index.json"
    if not os.path.exists(title):
        print("DOWNLOAD Japanese Name json file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

def download_image():
    url = "http://up.gc-img.net/post_img_web/2013/08/DYe8z4FT1xTCFeE_17563_20.jpeg"
    title = "keras-vgg16-model_01.jpg"
    if not os.path.exists(title):
        print("DOWNLOAD image file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

# ���f�����\�z����
model = VGG16()
model.summary()

#�C���v�b�g�̌`���m�F����
# model.input_shape (None, 224, 224, 3)


# �摜��ǂݍ��݁A���f���̓��̓T�C�Y�Ń��T�C�Y


# PIL.Image �I�u�W�F�N�g�� np.float32 �^�� numpy �z��ɕϊ�


# �z��̌`��� (Height, Width, Channels) ���� (1, Height, Width, Channels) �ɕύX


# �O����


# preds.shape: (1, 1000)


#�摜��\������


#�\���������O��\��


#���{��t�@�C�����_�E�����[�h

    
# ImageNet �̃��x���ꗗ��ǂݍ���
)

# ���_����


# ���_���ʂ�\��


