
# Stimulus exercise: 
# 1. 
from psychopy import visual, monitors, event

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon, units = 'pix') #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

import numpy as np #for random shuffling
stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images
#create the stimulus but don't specify the precise image yet
my_image = visual.ImageStim(win, units = 'pix')


np.random.shuffle(stims) #shuffle order of stims

for trial in range(nTrials): #loop through trials
    
    #point to a different filename for each image
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.size= 400,400
    my_image.draw() #draw
    win.flip() #show
    event.waitKeys() #wait for keypress
    
win.close() #close the window after all trials have looped  


# 3. 




#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
fixation = visual.textStim(win, text ='+')

#=====================
#START EXPERIMENT
#=====================
print('welcome')
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
    #-present block start message
    #-randomize order of trials here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
        
        #=====================
        #START TRIAL
        #=====================  
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window