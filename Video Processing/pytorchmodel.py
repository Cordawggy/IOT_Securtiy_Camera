# For model building, training and evaluation
import torch
import torch.nn as nn
import torch.optim as opt
from torch.utils.data import DataLoader, Dataset
import torchvision
import torchvision.transforms as trf
from torchvision.datasets import MNIST, ImageFolder
import timm

# General utils/visualization
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def systemInfo():
    print(f"Device: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")
    print(f"Python version: {sys.version}")
    print(f"Pytorch version: {torch.__version__}")
    print(f"Torchvision version: {torchvision.__version__}")
    print(f"Timm version: {timm.__version__}")
    print(f"OS: {os.name}")
    print(f"Numpy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")

if __name__ == "__main__":
    systemInfo()


