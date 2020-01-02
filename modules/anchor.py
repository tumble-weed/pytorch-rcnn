from matplotlib import pyplot as plt
import matplotlib.patches
from argparse import Namespace
import numpy as np

class BoundingBox():
    def __init__(self,**kwargs):
        self.set(**kwargs)
        pass
    def __getattr__(self,attr):
        #print('in getattr')
        cls = self.__class__
        if attr not in self.__dict__:
            f = (attr + '_')
            #print(f,f in cls.__dict__)
            if f in cls.__dict__:
                return cls.__dict__[f](self)
    def width_(self):
        if 'width' not in self.__dict__:
            if  'hw' not in self.__dict__ and 'hh' not in self.__dict__:
                return None
            self.width = self.hw*2
        return self.width
    def height_(self):
        if 'height' not in self.__dict__:
            if  'hw' not in self.__dict__ and 'hh' not in self.__dict__:
                return None
            self.height = self.hh*2
        return self.height
    def topleft_(self):
        if 'topleft' not in self.__dict__:
            if  'center' not in self.__dict__ or any([k not in self.__dict__ for k in ['hh','hw']]):
                return None
            self.topleft = self.center.y - self.hh, self.center.x - self.hw
        return self.topleft
    def bottomright_(self):
        pass
    def bottomleft_(self):
        #print('here')
        if  'center' not in self.__dict__ or any([k not in self.__dict__ for k in ['hh','hw']]):
                return None
        self.bottomleft = Namespace()
        self.bottomleft.y, self.bottomleft.x = self.center.y + self.hh, self.center.x - self.hw
        return self.bottomleft
    def set(self,**kwargs):
        for k in kwargs:
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
        cy,cx = c
        center = Namespace()
        center.x,center.y = cx,cy
        bboxes.append(BoundingBox(center=center,hh=hh,hw=hw))
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
        if not hasattr(strides,'__getitem__'):
            strides = (strides,strides)
        self.strides = strides
        pass
    
    @classmethod
    def get_valid_centers(cls,
            grid_size,
            bbox_dims,
            stride):
        #import pdb;pdb.set_trace()
        height,width = bbox_dims
        left, right = width//2. , grid_size[1] - width//2.      
        top, bottom = height//2. , grid_size[0] - width//2.

        Y,X = np.meshgrid(np.arange(top,bottom,stride[0]),np.arange(left,right,stride[1]))
        return zip(Y.flatten(),X.flatten())
    @classmethod
    def generate_anchors(cls,
            base_size,
            scales,
            aspect_ratios,
            stride,
            grid_size):
        if len(grid_size) == 4:
            grid_size = grid_size[-2:]
        elif len(grid_size) == 2:
            pass
        else:
            raise NotImplementedError

        S,A = np.meshgrid(scales,aspect_ratios)
        S,A = S.flatten(),A.flatten()
        bboxes = []
        for s,a in zip(S,A):
            bbox_dims = [d*s*a for d in base_size]
            valid_centers = cls.get_valid_centers(grid_size,bbox_dims,stride)
            bboxes.extend(get_many_bboxes(valid_centers ,bbox_dims,stride))
            
            #import pdb; pdb.set_trace()
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
            anchors,
            ):
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
