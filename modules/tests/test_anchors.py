import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from modules.anchor import AnchorGenerator, get_many_bboxes,BoundingBox
import torch
from utils.visualization import visualize_anchors
#from utils.visualization import visualize_anchors
def _test_bounding_box():
    from argparse import Namespace
    topleft,bottomright = Namespace(),Namespace()
    topleft.y,topleft.x = 0,0
    bottomright.y,bottomright.x = 14,14
    bbox = BoundingBox(topleft=topleft,bottomright=bottomright)
    import pdb;pdb.set_trace()
    pass
def _test_valid_centers():
    centers = AnchorGenerator.get_valid_centers([224,224],[7,7],[2,2])
    centers = list(centers)
    import pdb;pdb.set_trace()
    pass

def _test_many_bboxes():
    grid_size =[224,224]
    bbox_dims = [7,7]
    stride = [2,2]
    centers = AnchorGenerator.get_valid_centers(grid_size,bbox_dims,stride)
    centers = list(centers)
    bboxes = get_many_bboxes(centers,bbox_dims,stride)
    import pdb;pdb.set_trace()
    pass

def test_anchors():
    
    dummy_grid = torch.ones((1,3,224,224)).float() 
    base_size = (7,7)
    scales = [1]
    aspect_ratios = [0.5]
    strides = 2
    anchor_generator = AnchorGenerator(base_size,
    scales,
    aspect_ratios,
    strides
    )

    anchors = anchor_generator(dummy_grid)
    #import pdb;pdb.set_trace()
    visualize_anchors(anchors)
    pass

#--------------------------
tests = [el for l,el in locals().items() if l.startswith('test_')]
for t in tests:
    t()
