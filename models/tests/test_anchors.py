from models import AnchorGenerator
import torch
def test_anchors():
    
    dummy_grid = torch.ones((1,3,224,224)).float() 
    scales = [1,2,0.5]
    aspect_ratios = []
    anchor_generator = AnchorGenerator(scales,
    aspect_ratios,
    stride
    )

    anchors = anchor_generator(dummy_grid)

    AnchorGenerator.visualize(anchors)
    pass

tests = [test_anchors]

for t in tests:
    t()
