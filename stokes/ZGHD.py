import numpy as np
from keras import models
from matplotlib import pyplot as plt
# 读取模型
model = models.load_model('model.h5')
# 读取数据
data = np.load('data.npy')
base = np.load('base.npy')
norm = np.load('norm.npy')
# 归一化
for i in range(data.shape[1]):
    data[:, i] = (data[:,i]-np.min(data[:,i]))/(np.max(data[:,i])-np.min(data[:,i]))
# 处理time_step
def generate_data(data, time_step,predict_step):
    x = []
    y = []
    for i in range(data.shape[0]-time_step-predict_step*2,data.shape[0]-time_step):
        x.append(data[i:i+time_step,:])
    x = np.array(x)
    return x
time_step = 15
predict_step = 5
x = generate_data(data, time_step=time_step,predict_step=predict_step)
print(x.shape)
# 预测
y_predict = model.predict(x)
print(y_predict.shape)
# 反归一化
for i in range(y_predict.shape[1]):
    y_predict[:,i] = y_predict[:,i]*norm[i]+base[i]

# 绘制预测图像
plt.plot(y_predict[:,0],label='predict')
plt.legend()
plt.show()
plt.plot(y_predict[:,1],label='predict')
plt.legend()
plt.show()
plt.plot(y_predict[:,2],label='predict')
plt.legend()
plt.show()
plt.plot(y_predict[:,3],label='predict')
plt.legend()
plt.show()
