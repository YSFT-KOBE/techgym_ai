#Tech-Gym-13-8-Q
#�f�B�[�v���[�j���O�摜���ފ�:CNN

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
%matplotlib inline

#url����Download�ł��Ȃ��Ƃ���github�ɓo�^����Ă���circle.npy���g�p����
url = "https://aidemystorageprd.blob.core.windows.net/data/5100_cnn_data/circle.npy"
local_filename, headers = urllib.request.urlretrieve(url)
X = np.load(local_filename)

#�~�̉摜��\������

# ��ݍ��ݑw

# �J�[�l��(�t�B���^)
W = np.array([[0,1,0],
              [0,1,0],
              [0,1,0]])

#�J�[�l���̉摜��\��

# ��ݍ���

#��ݍ��ݏ����������摜���̕\��

