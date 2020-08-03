#Tech-Gym-13-20-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�摜����

#
import sys, os, glob
import urllib.request
import tarfile
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
    
# ���ޑΏۂ̃J�e�S����I��
caltech_dir = "./101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

# �摜�T�C�Y���w��
image_w = 64 
image_h = 64
pixels = image_w * image_h * 3

# �摜�f�[�^��ǂݍ���
X = []
Y = []
for idx, cat in enumerate(categories):
    # ���x�����w��
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    # �摜
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
X = np.array(X)
Y = np.array(Y)

file_path_err = os.path.dirname("image")
if not os.path.exists(file_path_err):
    os.makedirs("./image", exist_ok=True)

# �w�K�f�[�^�ƃe�X�g�f�[�^�𕪂���
X_train, X_test, y_train, y_test = train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy", xy)

#print("ok,", len(Y))

