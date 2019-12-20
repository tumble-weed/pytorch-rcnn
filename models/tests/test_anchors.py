from models import AnchorGenerator

def test_anchors():
    
    dummy_grid = torch.ones((1,3,224,224)).float() 

    anchor_generator = AnchorGenerator(scales,
    aspect_ratio,
    stride
    )

    anchors = anchor_generator(dummy_grid)

    AnchorGenerator.visualize(anchors)
    pass

tests = [test_anchors]

for t in tests:
    t()
