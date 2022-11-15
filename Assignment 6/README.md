
Dialogue box exercise:

fixed holds the value you have set for that varible constant, so in this case, it will default to 1 and be un-editable.

See the .py file for the code




Monitor and window exercise: 


1. height, norm, deg, cm, and pix are all ways of changing how we define our window. Each way has pros and cons, but in general, height uses cordinates that are dependent on the aspect ratio. norm uses cordinates of 1 and -1 for the edges of the window. cm uses cm on the screen, while pix uses the pixels on the screen to define the wondow.
2. Color space changes how you define your colour based on RGB, HSV, or DKL methods. Yes defining a colour by name is possible through the web/x11 colour names, defning a colour space in these cases is not needed.  
3. Se .py for code 



Stimulus exercise: 



# Dialogue box experiment 

import os
os.chdir('/User/shafamazidi/Desktop/Psych Python/psychopy stuff/Showing Windows and Stimuli')
main_dir = os.getcwd()

#=====================
#COLLECT PARTICIPANT INFO
#=====================

from psychopy import gui
from datetime import datetime
date = datetime.now()
#  to make an empty text entry varible, use the gender format.
exp_info = {'subject_nr':0, 'session':1,'age':0, 'handedness':('right','left','ambi'), 'gender':()}

# the only part you really need here is to define wich dictionary you are pulling from. The other paramters are optional. 
# If multiple varibles are being included in a parameter, you need to surround them by square brackets to make them a list, like oreder here. 
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = 'Subject Info', fixed= "session", order = ['session', 'subject_nr', 'age', 'handedness'], show = False)

print ('All variables have been created! Now ready to show the dialog box!')

show_dlg = my_dlg.show()

# this appends date and time 
date = datetime.now()
exp_info['date'] = str(date.day) + str(date.month) + str(date.year) 

#this creates a unique file name for the paprticipants data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv' # it needs to be a string
print('filename')
sub_dir = os.path.join(main_dir,'sub_info',filename)




# Monitor and window exersise 



#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width=35.56, distance=60) 
#use x,y coordinates to specify the pixel resolution of your monitor
mon.setSizePix([1600,900])

# the only part that is actually nessessary is the window is to define the window pixel size, which is the same as our monitor.  
win = visual.Window(monitor=mon)



# Stimulus exercise: 

1. This will make all the images square, hoever if you want to preserve their dimentions, then you can simply leave out the units, and multiply he image size by whatever constant you want. However the drawback of this is it is difficult to set min an max pixels for that image. 

2. see .py stimulus code 

3. see .py stimulus code 

4. see .py stimulus code 




