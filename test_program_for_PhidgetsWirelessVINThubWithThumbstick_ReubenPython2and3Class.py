# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision H, 12/31/2025

Verified working on: Python 3.12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#########################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
#########################################################

#########################################################
from MyPrint_ReubenPython2and3Class import *
from PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import traceback
import keyboard
#########################################################

#########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global PhidgetsWirelessVINThubWithThumbstick_Object
    global PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG
    global SHOW_IN_GUI_PhidgetsWirelessVINThubWithThumbstick_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:

        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG == 1 and SHOW_IN_GUI_PhidgetsWirelessVINThubWithThumbstick_FLAG == 1:
                PhidgetsWirelessVINThubWithThumbstick_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global PhidgetsWirelessVINThubWithThumbstick_Object
    global PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsWirelessVINThubWithThumbstick
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_PhidgetsWirelessVINThubWithThumbstick = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_PhidgetsWirelessVINThubWithThumbstick, text='   PhidgetsWirelessVINThubWithThumbstick   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_PhidgetsWirelessVINThubWithThumbstick = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    if PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG == 1:
        PhidgetsWirelessVINThubWithThumbstick_Object.CreateGUIobjects(TkinterParent=Tab_PhidgetsWirelessVINThubWithThumbstick)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    
    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_PhidgetsWirelessVINThubWithThumbstick_FLAG
    USE_PhidgetsWirelessVINThubWithThumbstick_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1
    
    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_PhidgetsWirelessVINThubWithThumbstick_FLAG
    SHOW_IN_GUI_PhidgetsWirelessVINThubWithThumbstick_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_PhidgetsWirelessVINThubWithThumbstick
    global GUI_COLUMN_PhidgetsWirelessVINThubWithThumbstick
    global GUI_PADX_PhidgetsWirelessVINThubWithThumbstick
    global GUI_PADY_PhidgetsWirelessVINThubWithThumbstick
    global GUI_ROWSPAN_PhidgetsWirelessVINThubWithThumbstick
    global GUI_COLUMNSPAN_PhidgetsWirelessVINThubWithThumbstick
    GUI_ROW_PhidgetsWirelessVINThubWithThumbstick = 1

    GUI_COLUMN_PhidgetsWirelessVINThubWithThumbstick = 0
    GUI_PADX_PhidgetsWirelessVINThubWithThumbstick = 1
    GUI_PADY_PhidgetsWirelessVINThubWithThumbstick = 1
    GUI_ROWSPAN_PhidgetsWirelessVINThubWithThumbstick = 1
    GUI_COLUMNSPAN_PhidgetsWirelessVINThubWithThumbstick = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsWirelessVINThubWithThumbstick
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsWirelessVINThubWithThumbstick_Object

    global PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG
    PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG = -1

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict = dict()

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DigitalInput0Object_State
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DigitalInput0Object_State = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = -11111.0

    global PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_Time
    PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global PhidgetsWirelessVINThubWithThumbstick_GUIparametersDict
    PhidgetsWirelessVINThubWithThumbstick_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_PhidgetsWirelessVINThubWithThumbstick_FLAG),
                                                                    ("EnableInternal_MyPrint_Flag", 0),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                    ("GUI_ROW", GUI_ROW_PhidgetsWirelessVINThubWithThumbstick),
                                                                    ("GUI_COLUMN", GUI_COLUMN_PhidgetsWirelessVINThubWithThumbstick),
                                                                    ("GUI_PADX", GUI_PADX_PhidgetsWirelessVINThubWithThumbstick),
                                                                    ("GUI_PADY", GUI_PADY_PhidgetsWirelessVINThubWithThumbstick),
                                                                    ("GUI_ROWSPAN", GUI_ROWSPAN_PhidgetsWirelessVINThubWithThumbstick),
                                                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_PhidgetsWirelessVINThubWithThumbstick)])

    global PhidgetsWirelessVINThubWithThumbstick_SetupDict
    PhidgetsWirelessVINThubWithThumbstick_SetupDict = dict([("GUIparametersDict", PhidgetsWirelessVINThubWithThumbstick_GUIparametersDict),
                                                            ("VINT_DesiredSerialNumber", -1), #-1 MEANS ANY SN, CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                            ("VINT_DesiredPortNumber", 4), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                            ("DesiredDeviceID", 63),
                                                            ("WaitForAttached_TimeoutDuration_Milliseconds", 15000),
                                                            ("NameToDisplay_UserSet", "Reuben's Test WiFi VINT with Thumbstick"),
                                                            ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                            ("MainThread_TimeToSleepEachLoop", 0.010),
                                                            ("UpdateDeltaT_ms", 20),
                                                            ("WirelessVINThub_ServerName_Str", "Phidgets_HUB5000_2AE182"),
                                                            ("WirelessVINThub_Address_Str", "192.168.100.1"), #hub5000.local #192.168.100.1 #Change to your IP address
                                                            ("WirelessVINThub_Port_Int", 5661), #Change to your port number
                                                            ("WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str", "AardvarkBadgerHedgehog"), #Change to your password
                                                            ("WirelessVINThub_Flags_Int", 0),
                                                            ("VoltageRatioInput0Object_SteadyStateOffset", 0.147),
                                                            ("VoltageRatioInput1Object_SteadyStateOffset", 0.018),
                                                            ("VoltageRatioInput0Object_LowPassFilter_Lambda", 0.95),
                                                            ("VoltageRatioInput1Object_LowPassFilter_Lambda", 0.95)])

    if USE_PhidgetsWirelessVINThubWithThumbstick_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            PhidgetsWirelessVINThubWithThumbstick_Object = PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class(PhidgetsWirelessVINThubWithThumbstick_SetupDict)
            PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG = PhidgetsWirelessVINThubWithThumbstick_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsWirelessVINThubWithThumbstick_Object __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################
    
    #################################################
    #################################################
    if USE_PhidgetsWirelessVINThubWithThumbstick_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG != 1:
                print("Failed to open PhidgetsWirelessVINThubWithThumbstick_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_GUIparametersDict
    MyPrint_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_SetupDict
    MyPrint_SetupDict = dict([("NumberOfPrintLines", 10),
                            ("WidthOfPrintingLabel", 200),
                            ("PrintToConsoleFlag", 1),
                            ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                            ("GUIparametersDict", MyPrint_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_PhidgetsWirelessVINThubWithThumbstick = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    print("Starting main loop 'test_program_for_PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG == 1:

            PhidgetsWirelessVINThubWithThumbstick_MostRecentDict = PhidgetsWirelessVINThubWithThumbstick_Object.GetMostRecentDataDict()

            if "Time" in PhidgetsWirelessVINThubWithThumbstick_MostRecentDict:
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["VoltageRatioInput0Object_VoltageRatio"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["VoltageRatioInput1Object_VoltageRatio"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DigitalInput0Object_State = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["DigitalInput0Object_State"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["DataStreamingFrequency_CalculatedFromMainThread"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback"]
                PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_Time = PhidgetsWirelessVINThubWithThumbstick_MostRecentDict["Time"]

                #print("PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_Time: " + str(PhidgetsWirelessVINThubWithThumbstick_MostRecentDict_Time))
        ###################################################
        ###################################################

        time.sleep(0.002)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting main program 'test_program_for_PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class.")

    #################################################
    if PhidgetsWirelessVINThubWithThumbstick_OPEN_FLAG == 1:
        PhidgetsWirelessVINThubWithThumbstick_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################