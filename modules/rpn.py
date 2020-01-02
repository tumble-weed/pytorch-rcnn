import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import torch
from matplotlib import pyplot as plt
import matplotlib.patches
from argparse import Namespace
import numpy as np
import models.rpn
import utils.misc as misc_utils

class RPN():
    def __init__(self,
            head,
            **config, 
            ):
        self.head = head
        self.rpn = rpn_models.get(**config)
        pass
    def forward(self,
            in_feats = None,
            in_image_tensor = None,
            in_image = None):
        assert not misc_utils.only_k_true([in_feats is not None,
            in_im_tensor is not None,
            in_image is None],1), 'provide only one of ...'
        if in_image is not None:
            in_feats = self.head(in_image = in_image)
        if in_image_tensor is not None:
            in_feats = self.head(in_image_tensor = in_image_tensor)
        return self.rpn(in_feats) 

