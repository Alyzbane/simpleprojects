import sys
import os
import glob
import webbrowser
import ctypes
import time
from datetime import datetime
from just_playback import Playback
from meetings_io import MeetingIO


MB_SYSTEMMODAL = 0x1000
MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10


""" GM-SC : Good Morning - Sexy Computer """
# Define a function to open a link
def open_link(link, code, weekday):
    notif.set_volume(1)
    notif.play();
    ctypes.windll.user32.MessageBoxW(0, f'{weekday} - {code}!!!', 'GM-CSOP' , MB_ICONEXCLAMATION) # refer to docs
    webbrowser.open_new_tab(link)

def csv_finder():
    dir = './'
    csv_files = glob.glob(os.path.join(dir, '*.csv'))
    if len(csv_files) != 0:
        return csv_files[0] # first csv file found will be return A-Z order
    ctypes.windll.user32.MessageBoxW(0, "No csv files found!", "Error", MB_SYSTEMMODAL | MB_ICONWARNING | MB_ICONERROR)
    sys.exit()

def start():
    notif = Playback('./alert.mp3')
    notif.set_volume(1)
    notif.play()
    ctypes.windll.user32.MessageBoxW(0, "GM-SC is running in the background...", 'CS-3A', MB_SYSTEMMODAL) # refer to docs

meetings = MeetingIO(csv_finder())
start()

while True:
    now = datetime.now()
    weekday = now.strftime('%A')
    ntime = now.strftime('%H:%M')

    if weekday in meetings:
        print(f"Weekday: {weekday}, Time: {ntime}")
        
        meeting_list = meetings.get(weekday, [])
        
        matching_meetings = [meeting for meeting in meeting_list if meeting[0] == ntime]
        
        for meeting_time, link, code in matching_meetings:
            print(f"Time: {meeting_time}, Link: {link}, Code: {code}")
            open_link(link, code, weekday)
            break

    """
     Idea: Modify time.sleep() by calculating the 
     refer to meetings_io.py and change the return dict
     {end_time - start_time} of class
    """
    time.sleep(60) # Wait for 1 minute before checking again
