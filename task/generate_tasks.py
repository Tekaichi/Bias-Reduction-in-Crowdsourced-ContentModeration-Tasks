# -*- coding: utf-8 -*-
"""
Generate Annotate and Verify tasks with n comments.
@author: Miguel Cardoso
"""


n = 5 # NUMBER OF COMMENTS IN A TASK


annotate = open("annotate-task-template.html", "r").read()
verify = open("verify-task-template.html","r").read()

task = open("task-template.html", "r").read().replace("{n}",str(n))

final_annotate = task
final_verify = task
body_annotate = ""
body_verify = ""
for i in range(n):
    body_annotate = body_annotate + annotate.replace("{n}",str(i+1))
    body_verify = body_verify + verify.replace("{n}",str(i+1))
final_annotate = final_annotate.replace("{TASK}",body_annotate)

f = open("annotate-task-"+str(n)+".html", "w+")
f.write(final_annotate)
f.close()

final_verify = final_verify.replace("{TASK}",body_verify)
f = open("verify-task-"+str(n)+".html", "w+")
f.write(final_verify)
f.close()