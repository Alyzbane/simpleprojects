# Prerequisites
`pip install -r requirements.txt`

## How to Run
**⚠️Make sure you have a .csv file in the same directory as the program⚠️**
- Double click on **gmcs.pyw**
- Press OK

### What's Happening?
If *time == meeting_time:*, a popup will open. Just press OK and the link will automatically open in the browser.

**The program is now running in the background and set to check the time every minute**

## Problems?
#### The meeting time has passed and there's still no popup alert
Check if it's running in the task manager: search for **python** and look at the background processes.

#### If it's not opening the right browser, change the default apps settings
Here's a guide: Change default programs in Windows
`search -> https -> pick your browser -> done!`

#### No mp3 files found
Put mp3 file in the current directory
If you want to use a file with a different extension, you'll need to change it in the code.

#### No csv files found
Put your csv meetings file in the current directory
Only csv files is accepted.

### Time is wrong
Just change 24 hour format into AM & PM
`15:00 19:00 (24h format) ❌`
`11:00 AM-09:00 PM (12h format) ✅`


