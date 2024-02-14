import sys
import os
import glob
import webbrowser
import ctypes
import time
import csv
from datetime import datetime
from just_playback import Playback
from collections import defaultdict

MB_SYSTEMMODAL = 0x1000
MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

""" GM-SC : Good Morning - Sexy Computer """
def find_file(ext=None):
    dir = './'

    if ext is None:
        print('Error: find_file() function no extension specified')
        sys.exit()

    files = glob.glob(os.path.join(dir, ext))
    if len(files) != 0:
        return files[0] # first csv file found will be return A-Z order

    ctypes.windll.user32.MessageBoxW(0, f"No {ext} files found!", "Error", MB_SYSTEMMODAL | MB_ICONWARNING | MB_ICONERROR)
    sys.exit()


"""
    Read csv file and return the following output format: 
            {'Day': [start time, link, subject code], ...}
    
    If csv file is from excel file:
    Issue sa cells ng link combined sa isa
    Walang Sakit: 
            Input:  Cell[1] Subject  [1] Link

            Output: Cell[1] Subject  [1] Link

    May Sakit: 
            Input:  Cell[1, 2] Subject [1] Link

            Output: Cell[1] Subject    [1] Link
                    Cell[2] Subject    [2] {}
"""

def MeetingIO(fr=None):
    meetings = defaultdict(list)

    if fr is None:
        fr = 'sched.csv'
        
    print(fr)
    with open(fr) as f:
        cr = csv.DictReader(f, delimiter=',')

        wkd_map = {
            'M': 'Monday',
            'T': 'Tuesday',
            'W': 'Wednesday',
            'H': 'Thursday',
            'F': 'Friday',
            'S': 'Saturday',
        }
        
        for row in cr:
            sub = row['SUBJECT']
            time = row['TIME']
            days = wkd_map[row['DAYS']]
            glink = row['GOOGLEMEET LINKS']

            st = time.split('-')[0].strip()
            hr, mn = map(int, st[:-2].split(':'))
            if "PM" in st[-2:] and hr != 12:
                hr += 12

            st = f'{hr:02d}:{mn:02d}'
            
            sb = sub.split(',')
            dl = days.split(',')
            tl = st.split(',')
            ll = glink.split(',')

            for sb, d, t, l in zip(sb, dl, tl, ll):
                meetings[d.strip()].append((t.strip(), l.strip(), sb.strip()))
    return meetings

def open_link(link, code, weekday):
    notif.play();
    ctypes.windll.user32.MessageBoxW(0, f'{weekday} - {code}!!!', 'GM-CSOP' , MB_SYSTEMMODAL | MB_ICONEXCLAMATION) # refer to docs
    webbrowser.open_new_tab(link)

def start():
    notif.play()
    ctypes.windll.user32.MessageBoxW(0, "GM-SC is running in the background...", 'CS-3A', MB_SYSTEMMODAL) # refer to docs

# ================ Main ========================
# Fix this xxxx

# Alert.mp3 for alarm notification sound
notif = Playback('./' + find_file('*.mp3'))
notif.set_volume(1)

meetings = MeetingIO(find_file('*.csv'))
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
