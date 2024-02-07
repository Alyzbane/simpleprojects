<h1>Prerequisites</h1>
<code>pip install -r requirements.txt</code>
<h2> How to Run </h2>
<strong>⚠️Make sure you have a .csv file in the same directory as the program⚠️</strong>
<ul>
<li>Double click on <strong>gmcs.pyw</strong></li>
<li>Press OK</li>
</ul> 
<h3> What's Happening? </h3>
<p>
If <i>time == meeting_time:</i>, a popup will open. Just press OK and the link will automatically open in the browser.
</p>
<strong>The program is now running in the background and is set to check the time every minute.</strong>
<h2>Problems?</h2>
<h4> The meeting time has passed and there's still no popup alert</h4>
<p> Check if it's running in the task manager: search for <strong>python</strong> and look at the background processes.</p>
<h4>If it's not opening the right browser, change the default apps settings</h4>
Here's a guide: https://support.microsoft.com/en-us/windows/change-default-programs-in-windows-e5d82cad-17d1-c53b-3505-f10a32e189
<code>search -> https -> pick your browser -> done!</code>
<h4>I want to change the alert sound</h4>
<p>Replace the alert.mp3 file with your desired file. Only mp3 files are accepted.
If you want to use a file with a different extension, you'll need to change it in the code.</p>
