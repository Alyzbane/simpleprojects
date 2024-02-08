from collections import defaultdict
import csv
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
