import torch
import torch.nn as nn
import torch.optim as optim

# 定义LSTM网络结构
class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.hidden_dim = hidden_dim

        # 定义LSTM层
        self.lstm = nn.LSTM(input_dim, hidden_dim)

        # 定义输出层
        self.linear = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # 初始化隐藏状态和细胞状态
        h0 = torch.zeros(1, x.size(1), self.hidden_dim)
        c0 = torch.zeros(1, x.size(1), self.hidden_dim)

        # 前向传播LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # 解码最后一个时间步的隐藏状态
        out = self.linear(out[-1, :, :])
        return out

# 超参数
input_dim = 5  # 输入维度
hidden_dim = 10  # 隐藏层维度
output_dim = 1  # 输出维度
num_epochs = 100  # 训练轮数
learning_rate = 0.001  # 学习率

# 实例化模型
model = LSTMModel(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 准备数据集（这里使用随机数据作为示例）
# 假设我们有100个序列，每个序列长度为10
# 每个时间步的输入特征维度为5
# 输出为单个值
X_train = torch.randn(100, 10, input_dim)
y_train = torch.randn(100, output_dim)

# 训练模型
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    # 反向传播和优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 测试模型（这里使用随机数据作为示例）
X_test = torch.randn(10, 10, input_dim)
y_test = model(X_test)
print(y_test)
