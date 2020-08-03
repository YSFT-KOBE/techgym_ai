#tech-gym-13-3-A
#�Z���T�[�f�[�^����

#�K�v�Ȃ��̂��C���|�[�g����
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.model_selection import train_test_split
import sklearn.svm

# �l���d�͂̓d�͏���ʃf�[�^��ǂݍ���
elec_data = pd.read_csv(
    'shikoku_electricity_2012.csv',
    skiprows=3,
    names=['DATE', 'TIME', 'consumption'],
    parse_dates={'date_hour': ['DATE', 'TIME']},
    index_col = "date_hour")

#�C�ۃf�[�^��ǂݍ���
tmp = pd.read_csv(
    u'takamatsu.csv',
    parse_dates={'date_hour': ["����"]},
    index_col = "date_hour",
    na_values="�~"
)

del tmp["��"]  # �u���v�̗�͎g��Ȃ��̂ŁA�폜

# ��̖��O���p��ɕύX
columns = {
    "�~����(mm)": "rain",
    "�C��(��)": "temperature",
    "���Ǝ���(h)": "sunhour",
    "���x(��)": "humid",
}
tmp.rename(columns=columns, inplace=True)

#�����l��-1�ɂ���
tmp.fillna(-1,inplace=True)

# ��, ��, ���̎擾
tmp["month"] = tmp.index.month
tmp['day'] = tmp.index.day
tmp['dayofyear'] = tmp.index.dayofyear
tmp['hour'] = tmp.index.hour

# �C�ۃf�[�^�Ɠd�͏���ʃf�[�^���������񓝍����Ď��Ԏ������킹�������ŁA�ēx����
takamatsu = elec_data.join(tmp[["temperature","sunhour","month","hour"]]).dropna().values

takamatsu_elec = takamatsu[:, 0:1]
takamatsu_wthr = takamatsu[:, 1:]

# �w�K�Ɛ��\�̕]��
model = sklearn.svm.SVR(gamma='scale')

x_train, x_test, y_train, y_test = train_test_split(
    takamatsu_wthr, takamatsu_elec, test_size=0.2)

y_train = y_train.flatten()
y_test = y_test.flatten()

model.fit(x_train, y_train)
date_name = ["�C��", "���Ǝ���","��","����"]

output = "�g�p���� = %s, �P���X�R�A = %f, ���؃X�R�A = %f" % \
         (", ".join(date_name),
          model.score(x_train, y_train),
          model.score(x_test, y_test)
          )

# �o��
print (output)
predicted = model.predict(x_test)
print(pd.DataFrame(predicted).describe())
print("���N���݂̋C���ł���΁A����345��kW�A�ő�438��kW���o����d�͂̐ݔ�����������΂悢")
