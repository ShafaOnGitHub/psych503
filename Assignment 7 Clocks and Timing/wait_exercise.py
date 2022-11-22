#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:06:28 2022

@author: shafamazidi
"""

from psychopy import core

  #=====================
        #START TRIAL
        #===================== 
        fixation = visual.Textstim(win, text = '+')
        fixation.draw()  #draw the fixation
        win.flip() #show
        core.wait(.5) #wait .5 seconds, then:
        
            
        my_image = visual.ImageStim(win)
        my_image.draw()#-draw image
        win.flip() #show
        core.wait(.5) #wait .5 seconds, then:
        
        end_message = visual.Textstim(win, text = 'the experiment is done')
        end_message.draw()
       win.flip() #show
       core.wait(.5) #wait .5 seconds, then: