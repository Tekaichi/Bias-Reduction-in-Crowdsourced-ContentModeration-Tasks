# Bias Reduction in Crowdsourced ContentModeration Tasks

Crowd Computing course group project @TU Delft, 2020.

## Authors
* Kanya Paramita Koesoemo
* Miguel Cardoso
* Beyza Hizli
* Guilherme Fonseca
* Manisha Sethia


## How to run : Summary
### Note: The following steps are to be done on Amazon Mechanical Turk
* Create a task and Copy paste Annotate-Justify.html to its design
* Create a task and Copy paste Verify-Justify.html to its design
* For each targeted location:
  *  Publish Annotate-Justify task with the location and select the dataset to be annotated.
* Retrieve results of Annotate-Justify per location
* For each Annotate-Justify Location:
  *  Publish Verify-Justify task to a different location and select Annotate-Justify results as its dataset, filtering out all the workers that participated in the Annotate-Justify, in the target location.

# How to run : Detailed 
### Platform 

This task is designed to be used on [Amazon Mechanical Turk](https://www.mturk.com/). Please create a requester account, log-in and visit [here](https://requester.mturk.com/create/projects/new)). 
Alternatively, if you wish to see a preview of the crowd-workers perspective, please log in [here](https://requester.mturk.com/developer/sandbox) instead.

### Creating the task - Verify
In Mtruk, create a new project. MTurk will allow you to edit the project. Do so, and you will see three tabs (Enter Properties, Design Layout and Preview and Finish). Please click on Design Layout and copy-paste the file "task/verify-task.html"). Enter your desired properties in the Enter properties tab. Select a location of you choose when recruiting the workers (in the Enter properties tab). To preview the task, go to the Preview and Finish tab. 

### Creating the task - Annotate-Justify
In Mtruk, create a new project. MTurk will allow you to edit the project. Do so, and you will see three tabs (Enter Properties, Design Layout and Preview and Finish). Please click on Design Layout and copy-paste the file "task/annotate-task.html"). Enter your desired properties in the Enter properties tab. Select a location of you choose when recruiting the workers (in the Enter properties tab). To preview the task, go to the Preview and Finish tab. 

### Sandbox
In Sandbox, create the task using the same process as described above. The only difference is that when Previewing the task, you will be able to see the Worker view. 

### Dataset
In the folder data, we have available three datasets to be used in the experimental setup. dataset-annotate.csv, which is meant for the Annotate-Justify task. verify-to-america.csv which is meant to the Verify-Task to be deployed in USA. verify-to-india.csv which is meant to the Verify-Justify to be deployed in India. Both the verify datasets are simulations of a biased first step.
