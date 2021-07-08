import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.pylab as pyl


data: object = pd.read_excel('E:\project\ju ZHEN\I.xls')
I = data.values

B = pd.read_excel('E:\project\ju ZHEN\B.xls')
B = B.values
C = I - B
C1 = np.linalg.inv(C)
T = B * C1
R = np.sum(T, axis=0)  # 各列之和
D = np.sum(T, axis=1)  # 各行之和
X = D + R
Y = D - R
T = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "b1", "b2", "b3", "c1", "c2"]
Xm=np.mean(X) #到了添加0刻线和阈值这一步

fig=plt.figure(figsize=(8,6)) #新建画布
ax=plt.subplot(1,1,1) #子图初始化
ax.scatter(X,Y) #绘制散点图
for i in range(len(Y)):
    ax.text(X[i] , Y[i] +0.01, T[i], fontsize=12, color="r", style="italic", weight="light",
            verticalalignment='center', horizontalalignment='right', rotation=0)  # 给散点加标签
plt.show()
