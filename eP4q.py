#tech-gym-13-1-Q
#�Z���T�[�f�[�^����

#�K�v�Ȃ��̂��C���|�[�g����
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

#�C�ۃf�[�^��ǂݍ���

# �u���v�̗�͎g��Ȃ��̂ō폜����
del tmp["��"]

# ��̖��O���p��ɕς���

#�����l��0�ɂ���

# �q�X�g�O��������

#�K�v�ɉ����ĕ\��
#display(tmp)

# �摜�T�C�Y��ݒ肷��
plt.figure(figsize=(20, 20))

# �\��
plt.subplot(3, 1, 1)
plt.scatter(tmp['time'], tmp['temperature'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('Temperature(C degree)')

plt.subplot(3, 1, 2)
plt.scatter(tmp['time'], tmp['humid'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('humid(%)')

plt.subplot(3, 1, 3)
plt.scatter(tmp['time'], tmp['rain'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('rain(mm)')


# �O���t�\��
plt.show()