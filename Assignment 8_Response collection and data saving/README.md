
# PsychoPy keypress exercises

1. An if key:
      response = key[0]       can be used. 
        
      print(response)
        
      It just collects the first key pressed within that trail, and prints that. See fixation and key press .py
        
        
 2. Putting event.clearEvents() outside the trial loop will not work to ignore responses when you want them to be ingnored. If you want responses to be ignored before a certain event in the trial, event.clearEvents() needs to be written right at the point in the trial at which you want to clear all reaponses that have been input. 

Unindenting the if key statements will make it so that it is outside of your trial loop. It wont work as anticipated by not being part of the for loop trial function. 


# Recording data exercises

1. Instead of filling a list, I have created a dictionary, my_dict, which prints each time a trial is completed. See recording data exercise.py 

2. I have created a dictionary called my_dict, and defined it in the block loop. See recording data exercise .py 


# Save csv exercise

Based on the csv.Dictwriter documentation, you can implement it as follows:

with open(fullAddress, 'w') as sub_data:
    fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time']
    data_writer = csv.DictWriter(sub_data, fieldnames=fieldnames)
    data_writer.writeheader()



# Read csv exercise (as discussed in class, I am using a .csv file here)

1. first we have to load the data frame into python like this. Then we can use the sum of these trials by the by the total number of trials for the mean.    

import pandas as pd

df = pd.read_csv('assignment_csvfile.csv')
print(df)

print(sum(df['acc_trials']))/len(df['sub_resp'])

2. 

import pandas as pd

df = pd.read_csv('assignment_csvfile.csv')
print(df)

acc_trials = df.loc[df['sub_acc'] == 1] #show only trials on which subject was correct
print(acc_trials)

3. 
import pandas as pd

df = pd.read_csv('assignment_csvfile.csv')
print(df)

sub_resp = df.loc[df['sub_resp'] != 0]

print(sub_resp)




