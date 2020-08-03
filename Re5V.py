#tech-gym-13-2-A
#�Z���T�[�f�[�^����

#�K�v�Ȃ��̂��C���|�[�g����
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

# �l���d�͂̓d�͏���ʃf�[�^��ǂݍ���
elec_data = pd.read_csv(
    'shikoku_electricity_2012.csv',
    skiprows=3,
    names=['DATE', 'TIME', 'consumption'],
    parse_dates={'date_hour': ['DATE', 'TIME']},
    index_col = "date_hour")

# �摜�̃T�C�Y��ݒ肷��
plt.figure(figsize=(12, 12))

# ���n��O���t����
delta = elec_data.index - pd.to_datetime('2012/07/01 00:00:00')
elec_data['time'] = delta.days + delta.seconds / 3600.0 / 24.0

#�d�͏���ʂ̎��ԕω�
plt.subplot(2, 1, 1)
plt.scatter(elec_data['time'], elec_data['consumption'], s=1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('electricity consumption(*10000 kWh)')

# �q�X�g�O��������
plt.subplot(2, 1, 2)
plt.hist(elec_data['consumption'], bins=100, color="gray")
plt.xlabel('electricity consumption(*10000 kW)')
plt.ylabel(u'count')

# �O���t
plt.show()