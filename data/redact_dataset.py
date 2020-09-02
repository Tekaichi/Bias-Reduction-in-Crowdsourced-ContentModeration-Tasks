# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:51:25 2020

@author: msdc1
"""

import numpy as np
import pandas as pd
file = open("dataset.txt")

lines = ["\""+i.strip()+"\"" for i in file]

file.close()


include = [1,3,4,7,9,12,14,18,19,20,22,23,29,33,36,38,40,42,45,46,2,27,34]

include =[i-1 for i in include]


lines = np.array(lines)[include]


file = open("dataset-redacted.txt","w+")

for i in lines:
    file.write(i)
    file.write("\n")
file.close()


file = open("labels.csv")


df = pd.read_csv(file)  

df = df.iloc[include]

df.to_csv("labels-redacted.csv")


