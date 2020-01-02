import os
my_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.abspath(os.path.join(my_dir,'..'))
import sys
sys.path.append(models_dir)
import numpy as np
import torch
def test_load_resnet():
    im = torch.tensor(np.zeros((1,3,224,224),dtype=np.float32))
    from models import utils
    layers = utils.get_layers_till(name = 'resnet50',
        till=4,
        pretrained = True)
    head = torch.nn.Sequential(*layers)
    out = head(im)
    pass
tests = [test_load_resnet,
        ]
for t in tests:
    t()
