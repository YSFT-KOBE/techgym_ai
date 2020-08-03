#Tech-Gym-13-9-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
%matplotlib inline

#url����Download�ł��Ȃ��Ƃ���github�ɓo�^����Ă���circle.npy���g�p����
url = "https://aidemystorageprd.blob.core.windows.net/data/5100_cnn_data/circle.npy"
local_filename, headers = urllib.request.urlretrieve(url)
X = np.load(local_filename)

plt.imshow(X)
plt.title("The original image", fontsize=12)
plt.show()

# ��ݍ��ݑw
class Conv:
    # W��3x3�ŌŒ肵�Ă���Astrides��padding�͍l�����Ă��Ȃ�
    def __init__(self, W):
        self.W = W
    def f_prop(self, X):
        #�o�͗p�̍s���������
        out = np.zeros((X.shape[0]-2, X.shape[1]-2))
        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                x = X[i:i+3, j:j+3]
                # �v�f���Ƃ̐ς̍��v���Ƃ��Ă��܂�
                out[i,j] = np.dot(self.W.flatten(), x.flatten())
        return out

def show_image(G1,G2,G3,G4):
    plt.subplot(1,4,1); plt.imshow(G1)
    plt.subplot(1,4,2); plt.imshow(G2)
    plt.subplot(1,4,3); plt.imshow(G3)
    plt.subplot(1,4,4); plt.imshow(G4)

# �J�[�l��(�t�B���^)
W1 = np.array([[0,1,0],
               [0,1,0],
               [0,1,0]])

W2 = np.array([[0,0,0],
               [1,1,1],
               [0,0,0]])

W3 = np.array([[1,0,0],
               [0,1,0],
               [0,0,1]])

W4 = np.array([[0,0,1],
               [0,1,0],
               [1,0,0]])

show_image(W1,W2,W3,W4)
plt.suptitle("kernel", fontsize=12)
plt.show()

# ��ݍ���


