#tech-gym-13-1-A
#�Z���T�[�f�[�^����

#�K�v�Ȃ��̂��C���|�[�g����
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

#�C�ۃf�[�^��ǂݍ���
tmp = pd.read_csv(
    u'takamatsu.csv',
    parse_dates={'date_hour': ["����"]},
    index_col = "date_hour",
    na_values="�~"
)

# �u���v�̗�͎g��Ȃ��̂ō폜����
del tmp["��"]

# ��̖��O���p��ɕς���
columns = {
    "�~����(mm)": "rain",
    "�C��(��)": "temperature",
    "���x(��)": "humid",
}
tmp.rename(columns=columns, inplace=True)

#�����l��0�ɂ���
tmp = tmp.fillna(0)

# �q�X�g�O��������
delta = tmp.index - pd.to_datetime('2012/07/01 00:00:00')
tmp['time'] = delta.days + delta.seconds / 3600.0 / 24.0

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
