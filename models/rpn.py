from utils.types import RPNOut
from utils.misc import is_shape,ismodel
class Standard():
    def __init__(self,
            n_classes,
            n_reg,
            input = None
            ):
        if is_shape(input):
        if is_model(input):
            
        self.bbox_reg
        self.objectness
    def forward(self,x):
        bbox_reg = 0
        objectness = 0
        return RPNOut(bbox_reg,objectness)
        pass
    pass

def get(modelname = None,
        **config):
    return locals()[modelname](**config)
