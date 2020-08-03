#tech-gym-13-UP-3-Q
#�Z���T�[�f�[�^����

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# ���x�f�[�^
df = pd.read_csv("humiduity.csv")
#display(df)

#�O���t��
df = df.set_index('Time')

fig, ax = plt.subplots(figsize=(15, 10))

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10);
ax.scatter(df.index, df['Humidity'])

plt.show()

