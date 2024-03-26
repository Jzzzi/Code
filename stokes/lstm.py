import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
# 读取华能水电.csv文件数据
data = pd.read_csv('华能水电.csv')
# 创建一个二维数组
data = np.array(data)
data = data[:, 3:]
data = data.astype(np.float32)
base = np.array([])
norm = np.array([])
# 每一列归一化处理
for i in range(data.shape[1]):
    norm = np.append(norm,np.max(data[:,i])-np.min(data[:,i]))
    base = np.append(base,np.min(data[:,i]))
    data[:, i] = (data[:,i]-np.min(data[:,i]))/(np.max(data[:,i])-np.min(data[:,i]))
# print(data)
# print(norm)
# print(base.shape)
# print(norm.shape)

# 定义函数处理time_step时间步长的数据
def generate_data(data, time_step, predict_step):
    x = []
    y = []
    for i in range(data.shape[0]-time_step-predict_step):
        x.append(data[i:i+time_step,:])
        y.append(data[i+time_step:i+time_step+predict_step,:4])
    x = np.array(x)
    y = np.array(y)
    # 将y的形状从3维变为2维
    y = y.reshape((y.shape[0], y.shape[1]*y.shape[2]))
    return x, y
x,y = generate_data(data, 15,3)
print(x.shape)
print(y.shape)
# print(data.shape)
# print(x.shape)

# 创建LSTM模型
model = Sequential()
model.add(LSTM(units=10,input_shape=(x.shape[1], x.shape[2])))
model.add(Dense(y.shape[1],activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x, y, epochs=1000, batch_size=10)

# 保存模型
model.save('model.h5')
# 保存处理好的数据
np.save('base.npy', base)
np.save('norm.npy', norm)
np.save('data.npy', data)