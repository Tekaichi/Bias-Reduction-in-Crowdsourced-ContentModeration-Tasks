# -*- coding: utf-8 -*-
"""
Generate Annotate and Verify tasks with n comments.
@author: Miguel Cardoso
"""

#Parameters
n = 5 # NUMBER OF COMMENTS IN A TASK
start_attention_check = 2
interval_attention_check = 5

#--------------------------------
attention_check = interval_attention_check
attention_number = 0
annotate = open("annotate-task-template.html", "r").read()
verify = open("verify-task-template.html","r").read()
attention = open("attention-check.html","r").read()
task = open("task-template.html", "r").read().replace("{n}",str(n+1))

verify_training = open("verify-training.html","r").read()
annotate_training = open("annotate-training.html","r").read()

final_annotate = task.replace("{TRAINING}",annotate_training)
final_verify = task.replace("{TRAINING}",verify_training)
body_annotate = ""
body_verify = ""
for i in range(n):
    if(i == start_attention_check or attention_check == 0):
        body_verify = body_verify + attention.replace("{n}",str(i+1)).replace("{an}",str(attention_number+1))
        body_annotate = body_annotate + attention.replace("{n}",str(i+1)).replace("{an}",str(attention_number+1))

        attention_check = interval_attention_check
        attention_number = attention_number + 1
    else:
        body_annotate = body_annotate + annotate.replace("{n}",str(i+1)).replace("{ln}",str(i+1-attention_number))
        body_verify = body_verify + verify.replace("{n}",str(i+1)).replace("{ln}",str(i+1-attention_number))
        attention_check = attention_check - 1
final_annotate = final_annotate.replace("{TASK}",body_annotate)

f = open("annotate-task-"+str(n)+".html", "w+")
f.write(final_annotate)
f.close()

final_verify = final_verify.replace("{TASK}",body_verify)
f = open("verify-task-"+str(n)+".html", "w+")
f.write(final_verify)
f.close()