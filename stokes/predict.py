import numpy as np
from keras import models
import matplotlib.pyplot as plt
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
def generate_data(data, time_step):
    x = []
    y = []
    for i in range(data.shape[0]-time_step):
        x.append(data[i:i+time_step,:])
        y.append(data[i+time_step,:4])
    x = np.array(x)
    y = np.array(y)
    return x, y
x,y = generate_data(data, 10)
# 预测
y_predict = model.predict(x)
# 反归一化
for i in range(y_predict.shape[1]):
    y_predict[:,i] = y_predict[:,i]*norm[i]+base[i]
    y[:,i] = y[:,i]*norm[i]+base[i]

# 比较预测和实际
plt.plot(y[:,0],label='true')
plt.plot(y_predict[:,0],label='predict')
plt.legend()
plt.show()

plt.plot(y[:,1],label='true')
plt.plot(y_predict[:,1],label='predict')
plt.legend()
plt.show()

plt.plot(y[:,2],label='true')
plt.plot(y_predict[:,2],label='predict')
plt.legend()
plt.show()

plt.plot(y[:,3],label='true')
plt.plot(y_predict[:,3],label='predict')
plt.legend()
plt.show()


print(y_predict[-1,:])
# 预测下一个数据点
x_predict = data[-10:,:]
x_predict = x_predict.reshape((1, x_predict.shape[0], x_predict.shape[1]))
y_predict = model.predict(x_predict)
for i in range(y_predict.shape[1]):
    y_predict[:,i] = y_predict[:,i]*norm[i]+base[i]
print(y_predict)