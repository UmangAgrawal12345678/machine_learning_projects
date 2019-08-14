import numpy as np 
import pandas as pd

p1 =np.array([[1,2],[3,4]])
print p1

p2 = np.array([1,2,3,4,5],ndmin=3)
print p2

p3 = np.array([1,2,3],dtype=complex)
print p3

p4 = pd.Series(p3)
print p4

data = {"name":["Ram","Shyam","Umang"],"Age":[23,34,23]}
p5 = pd.DataFrame(data,["rank1","rank2","rank3"])
print p5