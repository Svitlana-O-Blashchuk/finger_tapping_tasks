﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on February 20, 2025, at 14:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.1'
expName = 'complex finger tapping'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\UHASSELT\\1. PhD\\Motor task\\5. Index-middle finger tapping_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('WelcomeStart') is None:
        # initialise WelcomeStart
        WelcomeStart = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='WelcomeStart',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('resp_2') is None:
        # initialise resp_2
        resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_2',
        )
    if deviceManager.getDevice('resp_3') is None:
        # initialise resp_3
        resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_3',
        )
    # create speaker 'beep_sound_3_5Hz'
    deviceManager.addDevice(
        deviceName='beep_sound_3_5Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=8.0
    )
    # create speaker 'beep_sound_3_5Hz_2'
    deviceManager.addDevice(
        deviceName='beep_sound_3_5Hz_2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=8.0
    )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    WelcomeText = visual.TextStim(win=win, name='WelcomeText',
        text='Welcome to the Study!\n\nThe study consists of alternating blocks of sequential index-middle figer tapping and rest.\n\nWhen the word "TAP" appears on the screen, please tap your fingers in sequence Index → Middle → Index → Middle..... as quickly and accurately as possible.\n\nYou will have 30 seconds to complete each tapping block.\n\n During the whole duration of the task focus on the cross in the center of the screen.\n\nIf you are ready to begin, tap ANY BUTTON.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.7, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    WelcomeStart = keyboard.Keyboard(deviceName='WelcomeStart')
    
    # --- Initialize components for Routine "Setting" ---
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    text_16 = visual.TextStim(win=win, name='text_16',
        text='The first tapping block will start soon. Stay prepared!\n\nWhen you see the word "TAP" you may start tapping.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "tapping" ---
    resp_2 = keyboard.Keyboard(deviceName='resp_2')
    resp_3 = keyboard.Keyboard(deviceName='resp_3')
    text_15 = visual.TextStim(win=win, name='text_15',
        text='TAP',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    beep_sound_3_5Hz = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=False, 
        hamming=True, 
        speaker='beep_sound_3_5Hz',    name='beep_sound_3_5Hz'
    )
    beep_sound_3_5Hz.setVolume(1.0)
    
    # --- Initialize components for Routine "Rest_30" ---
    Rest30 = visual.TextStim(win=win, name='Rest30',
        text='REST',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_8 = visual.TextStim(win=win, name='text_8',
        text='5',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_9 = visual.TextStim(win=win, name='text_9',
        text='4',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_10 = visual.TextStim(win=win, name='text_10',
        text='3',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_11 = visual.TextStim(win=win, name='text_11',
        text='2',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_12 = visual.TextStim(win=win, name='text_12',
        text='1',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    beep_sound_3_5Hz_2 = sound.Sound(
        'A', 
        secs=0.2, 
        stereo=False, 
        hamming=True, 
        speaker='beep_sound_3_5Hz_2',    name='beep_sound_3_5Hz_2'
    )
    beep_sound_3_5Hz_2.setVolume(1.0)
    
    # --- Initialize components for Routine "End_screen" ---
    EndText = visual.TextStim(win=win, name='EndText',
        text='Thank you',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome.started', globalClock.getTime(format='float'))
    WelcomeStart.keys = []
    WelcomeStart.rt = []
    _WelcomeStart_allKeys = []
    # keep track of which components have finished
    WelcomeComponents = [WelcomeText, WelcomeStart]
    for thisComponent in WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WelcomeText* updates
        
        # if WelcomeText is starting this frame...
        if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeText.frameNStart = frameN  # exact frame index
            WelcomeText.tStart = t  # local t and not account for scr refresh
            WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WelcomeText.started')
            # update status
            WelcomeText.status = STARTED
            WelcomeText.setAutoDraw(True)
        
        # if WelcomeText is active this frame...
        if WelcomeText.status == STARTED:
            # update params
            pass
        
        # *WelcomeStart* updates
        waitOnFlip = False
        
        # if WelcomeStart is starting this frame...
        if WelcomeStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeStart.frameNStart = frameN  # exact frame index
            WelcomeStart.tStart = t  # local t and not account for scr refresh
            WelcomeStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WelcomeStart.started')
            # update status
            WelcomeStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(WelcomeStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(WelcomeStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if WelcomeStart.status == STARTED and not waitOnFlip:
            theseKeys = WelcomeStart.getKeys(keyList=['6', '7', '8', '9', '0', 'num_6', 'num_7', 'num_8', 'num_9', 'num_0'], ignoreKeys=["escape"], waitRelease=False)
            _WelcomeStart_allKeys.extend(theseKeys)
            if len(_WelcomeStart_allKeys):
                WelcomeStart.keys = _WelcomeStart_allKeys[-1].name  # just the last key pressed
                WelcomeStart.rt = _WelcomeStart_allKeys[-1].rt
                WelcomeStart.duration = _WelcomeStart_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome.stopped', globalClock.getTime(format='float'))
    # check responses
    if WelcomeStart.keys in ['', [], None]:  # No response was made
        WelcomeStart.keys = None
    thisExp.addData('WelcomeStart.keys',WelcomeStart.keys)
    if WelcomeStart.keys != None:  # we had a response
        thisExp.addData('WelcomeStart.rt', WelcomeStart.rt)
        thisExp.addData('WelcomeStart.duration', WelcomeStart.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Setting" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Setting.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    SettingComponents = [key_resp, text_16]
    for thisComponent in SettingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Setting" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['5', 'T', 't', 'num_5'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_16* updates
        
        # if text_16 is starting this frame...
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_16.started')
            # update status
            text_16.status = STARTED
            text_16.setAutoDraw(True)
        
        # if text_16 is active this frame...
        if text_16.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SettingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Setting" ---
    for thisComponent in SettingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Setting.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Setting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "tapping" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('tapping.started', globalClock.getTime(format='float'))
        resp_2.keys = []
        resp_2.rt = []
        _resp_2_allKeys = []
        resp_3.keys = []
        resp_3.rt = []
        _resp_3_allKeys = []
        beep_sound_3_5Hz.setSound('A', secs=0.2, hamming=True)
        beep_sound_3_5Hz.setVolume(1.0, log=False)
        beep_sound_3_5Hz.seek(0)
        # Run 'Begin Routine' code from code_15
        # Reset trial-specific variables
        repeat_count = 0           # Count how many beeps have been played
        next_beep_time = 0         # Schedule when the next beep should play
        sound_times = []           # List to store timestamps for each beep
        
        # Reset the sound component’s timing if needed.
        # For sound components created in Builder, you can clear the tStartRefresh property:
        beep_sound_3_5Hz.tStartRefresh = None
        
        # If your design allows, you might want to reinitialize some internal state here.
        
        # keep track of which components have finished
        tappingComponents = [resp_2, resp_3, text_15, beep_sound_3_5Hz]
        for thisComponent in tappingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tapping" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *resp_2* updates
            waitOnFlip = False
            
            # if resp_2 is starting this frame...
            if resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_2.frameNStart = frameN  # exact frame index
                resp_2.tStart = t  # local t and not account for scr refresh
                resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp_2.started')
                # update status
                resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
            if resp_2.status == STARTED and not waitOnFlip:
                theseKeys = resp_2.getKeys(keyList=['num_7','7'], ignoreKeys=["escape"], waitRelease=False)
                _resp_2_allKeys.extend(theseKeys)
                if len(_resp_2_allKeys):
                    resp_2.keys = [key.name for key in _resp_2_allKeys]  # storing all keys
                    resp_2.rt = [key.rt for key in _resp_2_allKeys]
                    resp_2.duration = [key.duration for key in _resp_2_allKeys]
            
            # *resp_3* updates
            waitOnFlip = False
            
            # if resp_3 is starting this frame...
            if resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_3.frameNStart = frameN  # exact frame index
                resp_3.tStart = t  # local t and not account for scr refresh
                resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp_3.started')
                # update status
                resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_3.clock.reset)  # t=0 on next screen flip
            if resp_3.status == STARTED and not waitOnFlip:
                theseKeys = resp_3.getKeys(keyList=['num_8','8'], ignoreKeys=["escape"], waitRelease=False)
                _resp_3_allKeys.extend(theseKeys)
                if len(_resp_3_allKeys):
                    resp_3.keys = [key.name for key in _resp_3_allKeys]  # storing all keys
                    resp_3.rt = [key.rt for key in _resp_3_allKeys]
                    resp_3.duration = [key.duration for key in _resp_3_allKeys]
            
            # *text_15* updates
            
            # if text_15 is starting this frame...
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_15.started')
                # update status
                text_15.status = STARTED
                text_15.setAutoDraw(True)
            
            # if text_15 is active this frame...
            if text_15.status == STARTED:
                # update params
                pass
            
            # if beep_sound_3_5Hz is starting this frame...
            if beep_sound_3_5Hz.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                beep_sound_3_5Hz.frameNStart = frameN  # exact frame index
                beep_sound_3_5Hz.tStart = t  # local t and not account for scr refresh
                beep_sound_3_5Hz.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('beep_sound_3_5Hz.started', t)
                # update status
                beep_sound_3_5Hz.status = STARTED
                beep_sound_3_5Hz.play()  # start the sound (it finishes automatically)
            
            # if beep_sound_3_5Hz is stopping this frame...
            if beep_sound_3_5Hz.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > beep_sound_3_5Hz.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    beep_sound_3_5Hz.tStop = t  # not accounting for scr refresh
                    beep_sound_3_5Hz.tStopRefresh = tThisFlipGlobal  # on global time
                    beep_sound_3_5Hz.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('beep_sound_3_5Hz.stopped', t)
                    # update status
                    beep_sound_3_5Hz.status = FINISHED
                    beep_sound_3_5Hz.stop()
            # update beep_sound_3_5Hz status according to whether it's playing
            if beep_sound_3_5Hz.isPlaying:
                beep_sound_3_5Hz.status = STARTED
            elif beep_sound_3_5Hz.isFinished:
                beep_sound_3_5Hz.status = FINISHED
            # Run 'Each Frame' code from code_15
            # Get the current time in the routine (for example, using the routine timer)
            t = routineTimer.getTime()  # Ensure routineTimer is defined in your experiment
            
            # Play the beep repeatedly until 105 repeats are reached
            if repeat_count < 105:
                if t >= next_beep_time:
                    # Play the sound
                    beep_sound_3_5Hz.play()
                    
                    # Optionally print debugging information:
                    print("Beep played at t =", t, "; tStartRefresh =", beep_sound_3_5Hz.tStartRefresh)
                    
                    # Record the time when the sound is played
                    sound_times.append(t)
                    repeat_count += 1
                    
                    # Schedule next beep (adjust interval as needed)
                    next_beep_time += 0.286  
            else:
                continueRoutine = False  # End the routine once the beep has been played 105 times
            
            # Example: if you have any code that depends on tStartRefresh, check it first:
            if beep_sound_3_5Hz.tStartRefresh is not None:
                if t > beep_sound_3_5Hz.tStartRefresh + 0.2 - frameTolerance:
                    # Additional frame code if needed
                    pass
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tappingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tapping" ---
        for thisComponent in tappingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('tapping.stopped', globalClock.getTime(format='float'))
        # check responses
        if resp_2.keys in ['', [], None]:  # No response was made
            resp_2.keys = None
        trials.addData('resp_2.keys',resp_2.keys)
        if resp_2.keys != None:  # we had a response
            trials.addData('resp_2.rt', resp_2.rt)
            trials.addData('resp_2.duration', resp_2.duration)
        # check responses
        if resp_3.keys in ['', [], None]:  # No response was made
            resp_3.keys = None
        trials.addData('resp_3.keys',resp_3.keys)
        if resp_3.keys != None:  # we had a response
            trials.addData('resp_3.rt', resp_3.rt)
            trials.addData('resp_3.duration', resp_3.duration)
        # Run 'End Routine' code from code_15
        # Log the beep play times to your data file
        thisExp.addData("sound3_5Hz_play_times", sound_times)
        
        # the Routine "tapping" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Rest_30" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Rest_30.started', globalClock.getTime(format='float'))
        beep_sound_3_5Hz_2.setSound('A', secs=0.2, hamming=True)
        beep_sound_3_5Hz_2.setVolume(1.0, log=False)
        beep_sound_3_5Hz_2.seek(0)
        # Run 'Begin Routine' code from code_16
        # Reset trial-specific variables
        repeat_count = 0           # Count how many beeps have been played
        next_beep_time = 0         # Schedule when the next beep should play
        sound_times = []           # List to store timestamps for each beep
        
        # Reset the sound component’s timing if needed.
        # For sound components created in Builder, you can clear the tStartRefresh property:
        beep_sound_3_5Hz_2.tStartRefresh = None
        
        # If your design allows, you might want to reinitialize some internal state here.
        
        # keep track of which components have finished
        Rest_30Components = [Rest30, text_8, text_9, text_10, text_11, text_12, beep_sound_3_5Hz_2]
        for thisComponent in Rest_30Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Rest_30" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Rest30* updates
            
            # if Rest30 is starting this frame...
            if Rest30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Rest30.frameNStart = frameN  # exact frame index
                Rest30.tStart = t  # local t and not account for scr refresh
                Rest30.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rest30, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Rest30.started')
                # update status
                Rest30.status = STARTED
                Rest30.setAutoDraw(True)
            
            # if Rest30 is active this frame...
            if Rest30.status == STARTED:
                # update params
                pass
            
            # if Rest30 is stopping this frame...
            if Rest30.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rest30.tStartRefresh + 25-frameTolerance:
                    # keep track of stop time/frame for later
                    Rest30.tStop = t  # not accounting for scr refresh
                    Rest30.tStopRefresh = tThisFlipGlobal  # on global time
                    Rest30.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Rest30.stopped')
                    # update status
                    Rest30.status = FINISHED
                    Rest30.setAutoDraw(False)
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # if text_8 is stopping this frame...
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.tStopRefresh = tThisFlipGlobal  # on global time
                    text_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_8.stopped')
                    # update status
                    text_8.status = FINISHED
                    text_8.setAutoDraw(False)
            
            # *text_9* updates
            
            # if text_9 is starting this frame...
            if text_9.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.started')
                # update status
                text_9.status = STARTED
                text_9.setAutoDraw(True)
            
            # if text_9 is active this frame...
            if text_9.status == STARTED:
                # update params
                pass
            
            # if text_9 is stopping this frame...
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.tStopRefresh = tThisFlipGlobal  # on global time
                    text_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_9.stopped')
                    # update status
                    text_9.status = FINISHED
                    text_9.setAutoDraw(False)
            
            # *text_10* updates
            
            # if text_10 is starting this frame...
            if text_10.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.started')
                # update status
                text_10.status = STARTED
                text_10.setAutoDraw(True)
            
            # if text_10 is active this frame...
            if text_10.status == STARTED:
                # update params
                pass
            
            # if text_10 is stopping this frame...
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.tStopRefresh = tThisFlipGlobal  # on global time
                    text_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_10.stopped')
                    # update status
                    text_10.status = FINISHED
                    text_10.setAutoDraw(False)
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.tStopRefresh = tThisFlipGlobal  # on global time
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            
            # *text_12* updates
            
            # if text_12 is starting this frame...
            if text_12.status == NOT_STARTED and tThisFlip >= 29-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_12.started')
                # update status
                text_12.status = STARTED
                text_12.setAutoDraw(True)
            
            # if text_12 is active this frame...
            if text_12.status == STARTED:
                # update params
                pass
            
            # if text_12 is stopping this frame...
            if text_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_12.tStop = t  # not accounting for scr refresh
                    text_12.tStopRefresh = tThisFlipGlobal  # on global time
                    text_12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_12.stopped')
                    # update status
                    text_12.status = FINISHED
                    text_12.setAutoDraw(False)
            
            # if beep_sound_3_5Hz_2 is starting this frame...
            if beep_sound_3_5Hz_2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                beep_sound_3_5Hz_2.frameNStart = frameN  # exact frame index
                beep_sound_3_5Hz_2.tStart = t  # local t and not account for scr refresh
                beep_sound_3_5Hz_2.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('beep_sound_3_5Hz_2.started', t)
                # update status
                beep_sound_3_5Hz_2.status = STARTED
                beep_sound_3_5Hz_2.play()  # start the sound (it finishes automatically)
            
            # if beep_sound_3_5Hz_2 is stopping this frame...
            if beep_sound_3_5Hz_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > beep_sound_3_5Hz_2.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    beep_sound_3_5Hz_2.tStop = t  # not accounting for scr refresh
                    beep_sound_3_5Hz_2.tStopRefresh = tThisFlipGlobal  # on global time
                    beep_sound_3_5Hz_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('beep_sound_3_5Hz_2.stopped', t)
                    # update status
                    beep_sound_3_5Hz_2.status = FINISHED
                    beep_sound_3_5Hz_2.stop()
            # update beep_sound_3_5Hz_2 status according to whether it's playing
            if beep_sound_3_5Hz_2.isPlaying:
                beep_sound_3_5Hz_2.status = STARTED
            elif beep_sound_3_5Hz_2.isFinished:
                beep_sound_3_5Hz_2.status = FINISHED
            # Run 'Each Frame' code from code_16
            # Get the current time in the routine (for example, using the routine timer)
            t = routineTimer.getTime()  # Ensure routineTimer is defined in your experiment
            
            # Play the beep repeatedly until 105 repeats are reached
            if repeat_count < 105:
                if t >= next_beep_time:
                    # Play the sound
                    beep_sound_3_5Hz_2.play()
                    
                    # Optionally print debugging information:
                    print("Beep played at t =", t, "; tStartRefresh =", beep_sound_3_5Hz_2.tStartRefresh)
                    
                    # Record the time when the sound is played
                    sound_times.append(t)
                    repeat_count += 1
                    
                    # Schedule next beep (adjust interval as needed)
                    next_beep_time += 0.286  
            else:
                continueRoutine = False  # End the routine once the beep has been played 105 times
            
            # Example: if you have any code that depends on tStartRefresh, check it first:
            if beep_sound_3_5Hz_2.tStartRefresh is not None:
                if t > beep_sound_3_5Hz_2.tStartRefresh + 0.2 - frameTolerance:
                    # Additional frame code if needed
                    pass
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Rest_30Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Rest_30" ---
        for thisComponent in Rest_30Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Rest_30.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_16
        # Log the beep play times to your data file
        thisExp.addData("sound3_5Hz_2_play_times", sound_times)
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "End_screen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('End_screen.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    End_screenComponents = [EndText]
    for thisComponent in End_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End_screen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EndText* updates
        
        # if EndText is starting this frame...
        if EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndText.frameNStart = frameN  # exact frame index
            EndText.tStart = t  # local t and not account for scr refresh
            EndText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndText.started')
            # update status
            EndText.status = STARTED
            EndText.setAutoDraw(True)
        
        # if EndText is active this frame...
        if EndText.status == STARTED:
            # update params
            pass
        
        # if EndText is stopping this frame...
        if EndText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EndText.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                EndText.tStop = t  # not accounting for scr refresh
                EndText.tStopRefresh = tThisFlipGlobal  # on global time
                EndText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndText.stopped')
                # update status
                EndText.status = FINISHED
                EndText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_screen" ---
    for thisComponent in End_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('End_screen.stopped', globalClock.getTime(format='float'))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
