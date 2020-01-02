import torch
from utils import head as head_utils
from matplotlib import pyplot as plt
import matplotlib.patches
from argparse import Namespace
import numpy as np
class Head(torch.nn.Module):
    def __init__(self,base_network_info):
        torch.nn.Module.__init__(self)
        self.base_network_info = base_network_info
        self.layers = head_utils.get_layers_till(**base_network_info)
        pass
    def forward(self,x):
        for l in self.layers:
            x = l(x)
        return x
    pass



