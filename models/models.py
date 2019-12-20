import torch
import utils
class Head(torch.nn.Module):
    def __init__(self,base_network_info):
        torch.nn.Module.__init__(self)
        self.base_network_info = base_network_info
        self.layers = utils.get_layers_till(**base_network_info)
        pass
    def forward(self,x):
        for l in self.layers:
            x = l(x)
        return x
    pass

class RPN():
    def __init__(self):
        pass
    def forward(self):
        pass


class AnchorGenerator():
    def __init__(self,
            scales,
            aspect_ratios,
            strides):
        pass
    @classmethod
    def generate_anchors(cls,
            scales,
            aspect_ratios,
            strides,
            grid_size):
        pass

    def __call__(self,
            grid = None,
            grid_size = None,
            ):
        self.__class__.generate_anchors
            pass
        pass

    @classmethod
    def visualize(cls,
            anchors=None):
        if anchors is None:
            anchors =  
        pass   
    pass
