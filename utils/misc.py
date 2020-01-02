from argparse import Namespace
def only_k_true(flags,k):
    scores = []
    for f in flags:
        scores.append(1 if f else 0)
    return sum(scores) == k

def is_shape(x):
    raise NotImplementedError
    pass

def ismodel(x):
    raise NotImplementedError
    pass

def read_config():
    raise NotImplementedError
    pass
