import torch
from models.detector import get
class Detector():
    def __init__(self,
            **config
            ):
        self.detector = get(**config)
        pass
    def forward(self,):
        pass
    pass

