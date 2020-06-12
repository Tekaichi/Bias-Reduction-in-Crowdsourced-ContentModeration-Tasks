
"""
Create two datasets in csv format; one for India, and one for USA
@author: Miguel Cardoso
"""




import random
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


n = 5
redundancy = 2
max_times = 9

header = [ "comment_"+str((i+1))+",label_"+str((i+1))+",label_not_"+str((i+1)) for i in range(n)]
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


to_america = open("to_america.csv","w+")

to_america.write(header)
to_america.write("\n")

  

american_values = to_american_dataset.values


    

to_india = open("to_india.csv","w+")

to_india.write(header)
to_india.write("\n")

indian_values = to_india_dataset.values


output_size = redundancy * len(indian_values)-10

output_i = [[] for i in range(output_size)]
output_a = [[] for i in range(output_size)]
constraints = {}

for i in range(output_size):
    j = 0
    o_i = output_i[i]
    o_a = output_a[i]
    
    while(j  < n):
        index = random.randrange(len(indian_values))
        value_i = indian_values[index]
        value_a = american_values[index]
        #value_i[0] == value_a[0] == comment are the same.
        if(value_i[0] not in o_i):
          
            if(value_i[0] in constraints):
                if(constraints[value_i[0]] == max_times):
                    continue
                constraints[value_i[0]] +=1
            
                

            else:
                constraints[value_i[0]] = 1
            
            o_i.append(value_i[0])
            o_i.append(value_i[1])
            o_i.append(value_i[2])
        
            o_a.append(value_a[0])
            o_a.append(value_a[1])
            o_a.append(value_a[2])
            
            j = j + 1
    j = 0
    index = random.randrange(n)
    value = indian_values[index]
    o_i.append(value_i[0])
    o_i.append(value_i[2])
    o_i.append(value_i[1])
    o_i.append(value_i[3])
        
    o_a.append(value_a[0])
    o_a.append(value_a[2])
    o_a.append(value_a[1])
    o_a.append(value_a[3])
   
    while(j < 2):
        index = random.randrange(len(indian_values))
        value_i = indian_values[index]
        value_a = american_values[index]
        if(value_i[0] not in o_i):
            o_i.append(value_i[0])
            o_i.append(value_i[1])
            o_i.append(value_i[2])
            o_i.append(value_i[3])
            o_a.append(value_a[0])
            o_a.append(value_a[1])
            o_a.append(value_a[2])
            o_a.append(value_a[3])
            j = j + 1
    
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
