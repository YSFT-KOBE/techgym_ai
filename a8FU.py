#Tech-Gym-13-18-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^:���f���ۑ�

from sklearn import datasets, svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

# �A�����̃T���v���f�[�^��ǂݍ���
iris = datasets.load_iris()

# �f�[�^���w�K
model = svm.SVC()
model.fit(iris.data, iris.target)

# �w�K�ς݃f�[�^��ۑ�
joblib.dump(model, 'iris.pkl', compress=True)

# �ۑ������w�K�ς݃f�[�^�ƕ��ފ��ǂݍ���
clf = joblib.load('iris.pkl')

# �A�����̃T���v���f�[�^��ǂݍ���
iris = datasets.load_iris()

# �\������
pre = clf.predict(iris.data)

# ���𗦂𒲂ׂ�
print(accuracy_score(iris.target, pre))


