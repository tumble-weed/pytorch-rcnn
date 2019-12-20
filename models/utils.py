import torchvision
import torch

import os
my_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(my_dir,'..'))
import sys
sys.path.append(src_dir)
import utils

model_dict = {}

model_dict = {
        'resnet50':torchvision.models.resnet50,
        'vgg16':torchvision.models.vgg16,
        'mobilenet':None}
def get_layers_till(name,
        till,
        pretrained):

    model = model_dict[name](pretrained=pretrained)
    layers  = model.children()
    layers = list(layers)[:till]
    return layers

