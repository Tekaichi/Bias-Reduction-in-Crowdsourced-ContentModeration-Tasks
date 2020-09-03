# -*- coding: utf-8 -*-
"""
Generate Annotate and Verify tasks with n comments.
@author: Miguel Cardoso
"""

#Parameters
attention_checks = [7,14,21]
n = 23 +len(attention_checks)

n_attention_checks = 0
#--------------------------------

annotate = open("annotate-task-template.html", "r").read()
verify = open("verify-task-template.html","r").read()
task = open("task-template.html", "r").read().replace("{n}",str(n+1))

verify_training = open("verify-training.html","r").read()
annotate_training = open("annotate-training.html","r").read()
attention_check = open("attention-check.html","r").read()
final_annotate = task.replace("{TRAINING}",annotate_training)
final_verify = task.replace("{TRAINING}",verify_training)
body_annotate = ""
body_verify = ""
for i in range(n):
   
    
    if((i+1) in attention_checks):
        body_annotate = body_annotate + attention_check.replace("{n}",str(i+1))
        n_attention_checks = n_attention_checks+ 1
    else:
        body_annotate = body_annotate + annotate.replace("{n}",str(i+1)).replace("{ln}",str(i+1-n_attention_checks))
        body_verify = body_verify + verify.replace("{n}",str(i+1)).replace("{ln}",str(i+1-n_attention_checks))
final_annotate = final_annotate.replace("{TASK}",body_annotate)

f = open("annotate-task-"+str(n)+".html", "w+")
f.write(final_annotate)
f.close()

final_verify = final_verify.replace("{TASK}",body_verify)
f = open("verify-task-"+str(n)+".html", "w+")
f.write(final_verify)
f.close()