import webbrowser
import ctypes
import time
from datetime import datetime
from just_playback import Playback
from meetings_io import MeetingIO


""" GM-SC : Good Morning - Sexy Computer """
notif = Playback('./alert.mp3')
notif.set_volume(1)
notif.play()
ctypes.windll.user32.MessageBoxW(0, "GM-SC is running...", 'CS-3A', 0x1000) # refer to docs

# Define a function to open a link
def open_link(link, code, weekday):
    notif.set_volume(1)
    notif.play();
    ctypes.windll.user32.MessageBoxW(0, f'{weekday} - {code}!!!', 'GM-CSOP' , 0x1000) # refer to docs
    webbrowser.open_new_tab(link)

"""BSCS-3A
    SUBJECTS: 3
    CLASSES: 13 incl. LABS
    LABS: 2 T, F
"""

meetings = MeetingIO('sched.csv')

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
