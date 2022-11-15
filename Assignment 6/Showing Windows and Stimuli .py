# Dialogue box experiment 

import os
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

#show_dlg = my_dlg.show()

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
from psychopy import visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60) 
#use x,y coordinates to specify the pixel resolution of your monitor
mon.setSizePix([1600,900])

# the only part that is actually nessessary is the window is to define the wondow pixel size, which is the same as our monitor.  
win = visual.Window(monitor=mon)


