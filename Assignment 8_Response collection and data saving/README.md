
# PsychoPy keypress exercises

1. An if key:
        response = key[0]       can be used. 
        
        print(response)
        
        It just collects the first key pressed within that trail, and prints that. See fixation and key press .py
        
        
 2. Putting event.clearEvents() outside the trial loop will not work to ignore responses when you want them to be ingnored. If you want responses to be ignored before a certain event in the trial, event.clearEvents() needs to be written right at the point in the trial at which you want to clear all reaponses that have been input. 

Unindenting the if key statements will make it so that it is outside of your trial loop in way, by not being part of the for loop trial function. 


# Recording data exercises

1. Instead of filling a list, I have created a dictionary, my_dict, which prints each time a trial is completed. 

2. 

