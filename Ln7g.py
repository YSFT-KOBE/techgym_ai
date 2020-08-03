#Tech-Gym-13-23-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�ړ]�w�K:

#�K�v�Ȃ��̂��C���|�[�g
import os
import json
import numpy as np
import urllib.request
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
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
    title = "keras-model_01.jpg"
    if not os.path.exists(title):
        print("DOWNLOAD image file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

# ���f�����\�z����
model = MobileNetV2()

#�K�v�ɉ����ĕ\��
#model.summary()

#�C���v�b�g�̌`���m�F����
# model.input_shape (None, 224, 224, 3)
print('model.input_shape', model.input_shape)  

# �摜��ǂݍ��݁A���f���̓��̓T�C�Y�Ń��T�C�Y
download_image()
img_path = 'keras-model_01.jpg'
img = image.load_img(img_path, target_size=model.input_shape[1:3])

# PIL.Image �I�u�W�F�N�g�� np.float32 �^�� numpy �z��ɕϊ�
x = image.img_to_array(img)
print('x.shape: {}, x.dtype: {}'.format(x.shape, x.dtype))
# x.shape: (224, 224, 3), x.dtype: float32

# �z��̌`��� (Height, Width, Channels) ���� (1, Height, Width, Channels) �ɕύX
x = np.expand_dims(x, axis=0)
print('x.shape: {}'.format(x.shape))  # x.shape: (1, 224, 224, 3)

# �O����
x = preprocess_input(x)

# preds.shape: (1, 1000)
preds = model.predict(x)
print('preds.shape: {}'.format(preds.shape))

#�摜��\������
result = decode_predictions(preds, top=5)[0]

#�\���������O��\��
for _, name, score in result:
    print('{}: {:.2%}'.format(name, score))

#���{��t�@�C�����_�E�����[�h
download_json()
    
# ImageNet �̃��x���ꗗ��ǂݍ���
with open('./imagenet_class_index.json',encoding="utf-8") as f:
    data = json.load(f)
    class_names = np.array([row['ja'] for row in data])

# ���_����
scores = model.predict(x)[0]
top5_classes = scores.argsort()[-5:][::-1]

plt.axis('off')
plt.imshow(img)

# ���_���ʂ�\��
for name, score in zip(class_names[top5_classes], scores[top5_classes]):
    print('{}: {:.2%}'.format(name, score))


