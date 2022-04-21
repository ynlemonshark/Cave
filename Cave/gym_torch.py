import torch
import torch.nn as nn

print(torch.cuda.is_available())
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(device)

print(torch.cuda.device_count())
