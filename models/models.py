import torch
import utils
from matplotlib import pyplot as plt
import matplotlib.patches
from argparse import Namespace
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

class BoundingBox():
    def __init__(self,**kwargs):
        self.set(**kwargs)
        pass
    def __getattr__(self,attr):
        if attr not in self.__dict__:
            f = ('_'+attr)
            if f in self.__dict__:
                return self.__dict__[f](self)
    def _width(self):
        if 'width' not in self.__dict__:
            if  'hw' not in self.__dict__ and 'hh' not in self.__dict__:
                return None
            self.width = self.hw*2
        return self.width
    def _height(self):
        if 'height' not in self.__dict__:
            if  'hw' not in self.__dict__ and 'hh' not in self.__dict__:
                return None
            self.height = self.hh*2
        return self.height
    def _topleft(self):
        if 'topleft' not in self.__dict__:
            if  'center' not in self.__dict__ or any([k not in self.__dict__ for k in ['hh','hw']]):
                return None
            self.topleft = self.center.y - self.hh, self.center.x - self.hw
        return self.topleft
    def _bottomright(self):
        pass
    def _bottomleft(self):
        if  'center' not in self.__dict__ or any([k not in self.__dict__ for k in ['hh','hw']]):
                return None
        self.bottomleft = Namespace()
        self.bottomleft.y, self.bottomleft.x = self.center.y + self.hh, self.center.x - self.hw
        return self.bottomleft
    def set(self,**kwargs):
        for k in self.kwargs:
            self.__dict__[k] = kwargs[k]
        if all(['topleft' in kwargs,'bottomright' in kwargs]):
            out = self.__class__.from_tlbr(self.topleft,self.bottomright)
            self.center = Namespace()
            self.center.y,self.center.x = out.cy,out.cx
            self.hh = out.hh
            self.hw = out.hw
    @classmethod
    def from_tlbr(cls,tl,br):
        '''
        tl: topleft
        br: bottomright
        '''
        cy,cx = (tl.y + br.y )/2.,(tl.x+br.x) /2.
        hh,hw = (br.y - tl.y)/2.,(br.x-tl.x)/2.
        out = Namespace()
        for k in ['cx','cy','hh','hw']:
            out.__dict__[k] = locals()[k]
        return out
def get_many_bboxes(valid_centers ,bbox_dims,stride):
    bboxes = []
    for c in valid_centers:
        hh,hw = bbox_dims[0]/2.,bbox_dims[1]/2.
        cy,cx = valid_centers
        bboxes.append(BoundingBox(center={'y':cy,'x':cx},hh=hh,hw=hw))
        pass
    return bboxes
    pass
class AnchorGenerator():
    def __init__(self,
            base_size,
            scales,
            aspect_ratios,
            strides):
        self.base_size = base_size
        self.scales = scales
        self.aspect_ratios = aspect_ratios
        self.strides = strides
        pass
    
    @classmethod
    def get_valid_centers(cls,
            grid_size,
            height,
            width,
            stride):

        left, right = width//2. , grid_size[1] - width//2.      
        top, bottom = height//2. , grid_size[0] - width//2.

        Y,X = np.meshgrid(np.arange(top,bottom,stride),np.arange(left,right,stride))
        return zip(Y[:],X[:])
    @classmethod
    def generate_anchors(cls,
            base_size,
            scales,
            aspect_ratios,
            stride,
            grid_size):
        
        S,A = np.meshgrid(scales,aspect_ratios)
        S,A = S.flatten(),A.flatten()
        bboxes = []
        for s,a in zip(S,A):
            bbox_dims = [d*s*_ for d,_ in zip(base_size,a)]
            valid_centers = get_valid_centers(*bbox_dims,stride)
            bboxes.extend(get_many_bboxes(valid_centers ,bbox_dims,stride))
        return bboxes

    def __call__(self,
            grid = None,
            grid_size = None,
            ):
        assert not all([grid_size is None, grid is None]), 'both grid_size and grid can\'t be None'
        if grid_size is None:
            grid_size = grid.shape
        if len(grid_size) == 4:
            pass
        elif len(grid_size) == 3:
            raise NotImplementedError
        elif len(grid_size) == 2:
            raise NotImplementedError
        self.anchors =  self.__class__.generate_anchors(     self.base_size,
                self.scales,
                self.aspect_ratios,
                self.strides,
                grid_size)
        return self.anchors

    @classmethod
    def visualize(cls,
            anchors):
        pass

    def visualize(self,
            grid_size = None
            ):
        if self.anchors is None:
            if grid_size is None:
                return None
            self.anchors = cls.generate_anchors(
            self.base_size,
            self.scales,
            self.aspect_ratios,
            self.stride,
            self.grid_size) 
        f,ax = plt.subplots(1)
        for a in self.anchors:
            r = matplotlib.patches(a.bottomleft.x,
                    a.bottomleft.y,
                    a.width,
                    a.height)
            ax.add_patch(r)
        plt.show()

    pass
