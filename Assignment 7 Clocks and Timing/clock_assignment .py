# 1

from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

wait_timer = core.Clock()

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show    

nBlocks=2
nTrials=3



for trial in range(nTrials): #loops through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() 
    imgStartTime = wait_timer.getTime()
    core.wait(.5)  
    
    my_image.draw()
    imgEndTime = wait_timer.getTime()
    win.flip()
    core.wait(2)
    
    fix_text.draw()
    win.flip() 
    imgStartTime = wait_timer.getTime()
    core.wait(.5)  
    
    print("Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
win.close()



# 2



from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

wait_timer = core.Clock()

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show    

nBlocks=2
nTrials=3

waitTimer = core.Clock() #meta timer for stimulus 
stimTimer = core.Clock() #time the stimulus 

for trial in range(nTrials): #loops through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    
    stimTimer.reset()
    imgStartTime = wait_timer.getTime()
    while stimTimer.getTime() <=1:
        my_image.draw()
        win.flip()
    imgEndTime = waitTimer.getTime()
    
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    
    print("Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
win.close()

#3




from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

wait_timer = core.Clock()

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show    

nBlocks=2
nTrials=3

waitTimer = core.Clock() #meta timer for stimulus 
stimTimer = core.CountdownTimer() #time the stimulus 

for trial in range(nTrials): #loops through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    
    stimTimer.reset()
    stimTimer.add(2) #add two seconds
    imgStartTime = wait_timer.getTime()
    while stimTimer.getTime() <=0:
        my_image.draw()
        win.flip()
    imgEndTime = waitTimer.getTime()
    
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    
    print("Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
win.close()



# 4. 

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
#-import psychopy functions
#-import file save functions
#-(import other functions as necessary: os...)

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
#-stimulus names (and stimulus extensions, if images) *
#-stimulus properties like size, orientation, location, duration *
#-start message text *

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") *
#-create an empty list for participant responses (e.g., "on this trial, response was a 
    #X") *
#-create an empty list for response accuracy collection (e.g., "was participant 
    #correct?") *
#-create an empty list for response time collection *
#-create an empty list for recording the order of stimulus identities *
#-create an empty list for recording the order of stimulus properties *

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions

wait_timer = core.Clock() # and here we set the clock timer 

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show    

nBlocks=2
nTrials=3

waitTimer = core.Clock() #meta timer for stimulus 
stimTimer = core.Clock() #time the stimulus 
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press





#=====================
#BLOCK SEQUENCE
#=====================
for block in rang(nBlocks)
    #-present block start message
    blockTimer.reset() # blcok timer here
    blockStart = blockTimer.getTimer() # trial timer here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials): #loops through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    
    stimTimer.reset()
    imgStartTime = wait_timer.getTime()
    while stimTimer.getTime() <=1:
        my_image.draw()
        win.flip()
    imgEndTime = waitTimer.getTime()
    
    
    fix_text.draw()
    win.flip() 
    core.wait(.5)  
    

    

#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
win.close()
#-quit experiment




# Frame Based Timing exersice 




# 1. and 2.


from psychopy import visual, monitors, event, core

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

#set durations
fix_dur = 0.2 #200 ms
image_dur = 0.1 #100 ms
text_dur = 0.2 #200 ms

#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text='+')

nBlocks=1
nTrials=3

image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg','face02.jpg','face03.jpg'] 

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        
        my_image.image = os.path.join(image_dir,stims[trial])
    
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                my_image.draw()
                fix.draw() #draw
                win.flip() #show 
                
                if frameN == (fix_frames+image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show  
                
                if frameN == (total_frames-1): #last frame for the text
                    print("End text frame =", frameN) #print frame number    
                
    print('Overall, %i frames were dropped.' % win.nDroppedFrames)

win.close()                




