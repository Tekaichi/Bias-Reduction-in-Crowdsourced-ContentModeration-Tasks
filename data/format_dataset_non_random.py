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
labels = "labels.csv"




df = pd.read_csv(labels)  


file = open("dataset.txt")

lines = ["\""+i.strip()+"\"" for i in file]

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



redundancy = 5 #n of comments per row


header = [ "comment_"+str((i+1))+",label_"+str((i+1))+",label_not_"+str((i+1)) for i in range(redundancy)]
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


to_america = open("verify_to_america.csv","w+")

to_america.write(header)
to_america.write("\n")

  

american_values = to_american_dataset.values


    

to_india = open("verify_to_india.csv","w+")

to_india.write(header)
to_india.write("\n")

indian_values = to_india_dataset.values


scale = 1
output_size =  len(indian_values) *scale

output_i = [[] for i in range(output_size)]
output_a = [[] for i in range(output_size)]
constraints = {}

training_size = 3
attention_check = 1
#How to increase output size ? 
for i in range(output_size):
    for j in range(redundancy):
      
        index = (i+j)%len(indian_values)
        value_i = indian_values[index]
        value_a = american_values[index]
        output_i[i].append(value_i[0])
        output_i[i].append(value_i[1])
        output_i[i].append(value_i[2])
        #
        output_a[i].append(value_a[0])
        output_a[i].append(value_a[1])
        output_a[i].append(value_a[2])
        
    #Add training samples

    
    for j in range(training_size-attention_check):
        
        
        index = rand.randrange(output_size)
        
        value_i = indian_values[index]
        value_a = american_values[index]
        while(value_i[0] in output_i[i]):
            index = rand.randrange(output_size)
            
            value_i = indian_values[index]
            value_a = american_values[index]
        
        output_i[i].append(value_i[0])
        output_i[i].append(value_i[2])
        output_i[i].append(value_i[1])
        output_i[i].append(value_i[3])
        output_a[i].append(value_i[0])
        output_a[i].append(value_a[2])
        output_a[i].append(value_a[1])
        output_a[i].append(value_a[3])
    for j in range(attention_check):
        index = rand.randrange(redundancy)*3
    
        row = output_i[i]
        output_i[i].append(row[index])
        output_i[i].append(row[index+2])
        output_i[i].append(row[index+1])
        output_i[i].append(row[index+3])
        row = output_a[i]
        output_a[i].append(row[index])
        output_a[i].append(row[index+2])
        output_a[i].append(row[index+1])
        output_a[i].append(row[index+3])

        
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
to_india.close()
to_america.close()


annotate = open("dataset_annotate.csv","w+")

header = [ "comment_"+str((i+1)) for i in range(redundancy)]
header.append("comment_t_1")
header.append("truth_t_1")
header.append("comment_t_2")
header.append("truth_t_2")
header.append("comment_t_3")
header.append("truth_t_3")
header = ",".join(header)
annotate.write(header)
annotate.write("\n")

output_annotate = [[] for i in range(output_size)]
for i in range(output_size):
    for j in range(redundancy):
      
        index = (i+j)%len(indian_values)
        value= american_values[index]
        output_annotate[i].append(value[0])
  
        
    #Add training samples

    for j in range(training_size-attention_check):
        
        
        index = rand.randrange(output_size)
        
        value= american_values[index]
        while(value[0] in output_annotate[i]):
            index = rand.randrange(output_size)
            value= american_values[index]
        
        output_annotate[i].append(value[0])
        output_annotate[i].append(value[3])

    for j in range(attention_check):
        index = rand.randrange(redundancy)
        row = output_annotate[i]
        output_annotate[i].append(row[index])
        output_annotate[i].append(row[index+3])

        
output_annotate = [",".join(i) for i in output_annotate]
for i in output_annotate:
    annotate.write(i)
    annotate.write("\n")
    
annotate.close()
        
