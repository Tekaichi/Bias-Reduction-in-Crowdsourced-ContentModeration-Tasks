# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:06:06 2020

@author: msdc1
"""


# -*- coding: utf-8 -*-
"""
Create two datasets in csv format; one for India, and one for USA
@author: Miguel Cardoso
"""




import random as rand
import csv
import pandas as pd

def inverse(label):
    if(label == "Inappropriate"):
        return "Appropriate"
    return "Inappropriate"
labels = "labels-redacted.csv"




df = pd.read_csv(labels)  


file = open("dataset-redacted.txt")

lines = [i.strip() for i in file]

file.close()
comments = pd.DataFrame({'comments': lines})

to_american_dataset = df["=> USA"] 

to_american_dataset = comments.join(to_american_dataset)

to_american_dataset = to_american_dataset.rename(columns={"=> USA":"label"})

to_american_dataset_not = pd.DataFrame({"label_not":[inverse(i) for i  in to_american_dataset["label"].values]})

to_american_dataset = to_american_dataset.join(to_american_dataset_not)

to_american_dataset = to_american_dataset.join(df["Majority Voting"])

to_india_dataset = df["=> India"]

to_india_dataset = comments.join(to_india_dataset)

to_india_dataset = to_india_dataset.rename(columns={"=> India":"label"})

to_india_dataset_not = pd.DataFrame({"label_not":[inverse(i) for i  in to_india_dataset["label"].values]})

to_india_dataset = to_india_dataset.join(to_india_dataset_not)

to_india_dataset = to_india_dataset.join(df["Majority Voting"])



redundancy = 3 #n shuffle
training_size = 3

header = [ "comment_"+str((i+1))+",label_"+str((i+1))+",label_not_"+str((i+1)) for i in range(len(lines)-training_size)]
header.append("comment_t_1")
header.append("label_t_1")
header.append("label_not_t_1")
header.append("truth_t_1")
header.append("comment_t_2")
header.append("label_t_2")
header.append("label_not_t_2")
header.append("truth_t_2")
header.append("comment_t_3")
header.append("label_t_3")
header.append("label_not_t_3")
header.append("truth_t_3")
header = ",".join(header)


to_america = open("verify_to_america-{0}.csv".format(redundancy),"w+")

to_america.write(header)
to_america.write("\n")

  

american_values = to_american_dataset.values


    

to_india = open("verify_to_india-{0}.csv".format(redundancy),"w+")

to_india.write(header)
to_india.write("\n")

indian_values = to_india_dataset.values




output_i = [[] for i in range(redundancy)]
output_a = [[] for i in range(redundancy)]
constraints = {}



#How to increase output size ? 
for i in range(redundancy):
    row_a = to_american_dataset.iloc[:-training_size].sample(frac=1)
    row_i = to_india_dataset.iloc[:-training_size].sample(frac=1)
    for j in range(len(lines)-training_size):
      
  
        value_i = row_i.iloc[j]
        value_a = row_a.iloc[j]
        output_i[i].append(value_i[0])
        output_i[i].append(value_i[1])
        output_i[i].append(value_i[2])
        #
        output_a[i].append(value_a[0])
        output_a[i].append(value_a[1])
        output_a[i].append(value_a[2])
        
    #Add training samples
    row_a = to_american_dataset.iloc[-training_size:]
    row_i = to_india_dataset.iloc[-training_size:]
    for j in range(training_size):
        value_i = row_i.iloc[j]
        value_a = row_a.iloc[j]
        output_i[i].append(value_i[0])
        output_i[i].append(value_i[1])
        output_i[i].append(value_i[2])
        output_i[i].append(value_i[3])

        output_a[i].append(value_a[0])
        output_a[i].append(value_a[1])
        output_a[i].append(value_a[2])
        output_a[i].append(value_a[3])
output_a = [[j.strip() for j in i] for i in output_a]
output_i = [[j.strip() for j in i] for i in output_i]

india_ = output_i           
american_ = output_a
output_a = [",".join(i) for i in output_a]
output_i = [",".join(i) for i in output_i]

for i in output_i:
    to_india.write(i)
    to_india.write("\n")
for i in output_a:
    to_america.write(i)
    to_america.write("\n")
to_america.close()
to_india.close()


annotate = open("dataset_annotate.csv","w+")

header = [ "comment_"+str((i+1)) for i in range(len(lines)-training_size)]
header.append("comment_t_1")
header.append("truth_t_1")
header.append("comment_t_2")
header.append("truth_t_2")
header.append("comment_t_3")
header.append("truth_t_3")
header = ",".join(header)
annotate.write(header)
annotate.write("\n")

output_annotate = [[] for i in range(redundancy)]
for i in range(redundancy):
    row = to_american_dataset.iloc[:-training_size].sample(frac=1)
 
    for j in range(len(lines)-training_size):
      
        value= row.iloc[j]
        output_annotate[i].append(value[0])
  
        
    #Add training samples

    row = to_american_dataset.iloc[-training_size:]

    for j in range(training_size):
        value = row.iloc[j]
    
        output_annotate[i].append(value[0])
    
        output_annotate[i].append(value[3])

 

        
output_annotate = [",".join(i) for i in output_annotate]
for i in output_annotate:
    annotate.write(i)
    annotate.write("\n")
    
annotate.close()
        
