"""mastering numerical computing with numpy"""
import numpy as np
# first
x = np.array([[1, 0, 4], [3, 3, 1]])
y = np.array([[2, 5], [1, 1], [3, 2]])
print(x.dot(y))

##

x = np.array([[1, 0, 4], [3, 3, 1]], dtype=np.float)
print(x)
print(x.nbytes)
print(x.shape)
print(x.size)



##
Data_cancer=np.random.rand(100000,100)

print(type(Data_cancer))
print(Data_cancer.dtype)
print(Data_cancer.nbytes)

Data_cancer_New=np.array(Data_cancer,dtype=np.float32)
print(Data_cancer_New.nbytes)]



###
my_list=[2,4,12,3]

my_array=np.asarray(my_list)
type(my_array)
second_array=np.zeros(4)+3
second_array/my_array


##compare
x=np.array([2,3,3])
y=np.array([2,3,4])
x==y
np.array_equal(x,y)
print(x<y)


###
x=np.arange(9)
x=np.arange(9).reshape((3,3))
np.sum(x)
np.amin(x)
#最小要素
np.amin(x,axis=0)
np.amin(x,axis=1)
