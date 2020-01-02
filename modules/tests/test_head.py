import os
my_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.abspath(os.path.join(my_dir, '../'))
import sys
sys.path.append(models_dir)

import torch
device  = 'cuda' if torch.cuda.is_available() else 'cpu'
from models import Head,RPN
import numpy as np

im = torch.tensor(np.random.random((1,3,224,224)).astype(np.float32)).to(device)
def test_head():
    head = Head({'name':'resnet50',       
        'till':4,
        'pretrained':True})

    feats = head(im)
    print(feats.shape)
    pass
def test_rpn():
    head = Head()
    rpn = RPN(head)
    rpn_scores,rpn_bbox_coeff = rpn(im,otype='named_tuple')

    print(rpn_scores.shape,
            rpn_scores.sum(),
            rpn_scores.max(),
            rpn_scores.min())

    print(  rpn_bbox_coeff.shape,
            rpn_bbox_coeff['off_x'],
            rpn_bbox_coeff['off_y'],
            rpn_bbox_coeff['scale_x'],
            rpn_bbox_coeff['scale_y'],
            )
    pass

def test_anchors():
    head = Head()
    rpn = RPN(head)
    proposal_layer = ProposalLayer(rpn,
            scales = [],
            aspect_ratio = [])
    '''
    anchor_generator = AnchorGenerator(head,
            scales = [],
            aspect_ratios=[])

    anchors = anchor_generator.generate()
    '''
        
    pass
def test_anchors():
    head = Head()
    rpn = RPN(head)
    anchors = generate_anchors(rpn.stride,
            scales = [],
            aspect_ratio = [])
    pass
def test_crop_pooling():
    head = Head()
    feats  = head(im)
    gt_im_box = [] 
    pooled = crop_pool(feats,
            gt_im_box,
            head.stride)
    print(pooled.shape)
    pass
def test_clf():
     
    head = Head()
    rpn  = RPN(head)
    proposal = Proposal(rpn)
    clf = Clf(proposal)
    
    clf_scores, clf_bbox_coeff = clf(im,otype='named_tuple')
    pass
tests = [test_head,
        ]
for t in tests:
    t()
