me# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:27:39 2020

@author: Miguel Cardoso
"""
import pandas as pd
import collections

def getMax(dic):
    value = 0
    max_key = ""
    value_s = 0
    max_key_s = ""
    for key in dic:
        if(dic[key] == value):
            value_s = dic[key]
            max_key_s = key
        if(dic[key] > value):
            max_key = key
            value = dic[key]
        
    return (max_key,value),(max_key_s,value_s)

df = pd.read_csv('team_labels.csv')  

tmp = df.filter(regex="C.*")
df = df.drop(columns= tmp.columns)


freqs = {}

for i in df.values:
    freqs[i[0]] = collections.Counter(i[1:])

agreement = 0
max_labels = []
majority = {}
all_ = {}
for i in freqs:
    if (len(freqs[i]) == 1):
        agreement = agreement + 1
    row = freqs[i]
    for j in row:
        if(j not in all_):
            all_[j] = 0
        all_[j] = all_[j] + row[j]
        
    max_labels.append(getMax(freqs[i]))

df = pd.read_csv('labels.csv')  

df = df["Majority Voting"]
res = collections.Counter(df.values)