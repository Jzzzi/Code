import torch
import torch.cuda as cuda
import torch.nn as nn

print(cuda.is_available())
print(cuda.device_count())

# 输出cpu的名称
print(cuda.get_device_name(0))