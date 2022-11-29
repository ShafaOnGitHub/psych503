from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')



for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE, this makes it so no reponses before this line are noted
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?  So bascially what keys were pressed after the fixation
    
    if keys:
        sub_resp = keys[0] #only take first response
        
        print("responses that were counted", sub_resp)    
    
win.close()