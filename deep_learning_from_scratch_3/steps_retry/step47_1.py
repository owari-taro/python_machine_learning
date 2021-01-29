import sys
import os
sys.path.append(os.pardir)

import dezero.functions as F
import numpy as np
from dezero import Function,Variable


class GetItem(Function):
    def __init__(self, slices):
        self.slices = slices

    def forward(self, x):
        y = x[self.slices]
        return y

    def backward(self, gy):
        x, = self.inputs
        f = GetItemGrad(self.slices, x.shape)
        return f(gy)


def get_item(x, slices):
    return GetItem(slices)(x)


class GetItemGrad(Function):
    def __init__(self, slices, in_shape):
        self.slices = slices
        self.in_shape = in_shape

    def forward(self, gy):
        gx = np.zeros(self.in_shape)
        np.add.at(gx, self.slices, gy)

    def backward(self, ggx):
        return get_item(ggx, self.slices)

if __name__=="__main__":
    x=Variable(np.array([[1,2,3],[4,5,6]]))
    y=F.get_item(x,1)
    print(y)
