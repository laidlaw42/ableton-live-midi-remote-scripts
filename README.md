Scripts for creating custom MIDI Remote Scripts for Ableton Live.<br>
Known to be working on Live 9, untested on Live 10.<br>
<br>
<br>
<a href="https://youtu.be/IgKwcCJsoz4">In-depth video tutorial</a><br>
For the Push 2, user <a href="https://github.com/jzgdev/Push2UserModeScript">jzgdev</a> has a working Push 2 User Mode.<br>
<br>

<H4>Additional:</H4>
To change the size of the track selection box (coloured box in Session view):
Open “YourControllerName.py”<br>
Change the values in the brackets () of lines 94, 99, 100, 106 and 107 to suit your needs.<br>
<br>
On line 94 the first number is the amount horizontally and second is vertical.<br>
Lines 99 and 106 are vertical, 100 and 112 are horizontal. <br>
Make sure the value that you input corresponds with the two values on line 94. <br>
<br>
<br>
This is what the code will look like:<br>
94        self._session = SpecialSessionComponent(X, Y)<br>
99        self._scene_launch_buttons = [self._note_map[SCENELAUNCH[index]] for index in range(X) ]<br>
100       self._track_stop_buttons = [self._note_map[TRACKSTOP[index]] for index in range(Y) ]<br>
106       for scene_index in range(X):<br>
112       for track_index in range(Y):<br>
<br>
Lastly, don’t forget to add or remove rows/columns for SCENELAUNCH and CLIPNOTEMAP from MIDI_Map.py<br>
<br>
<br>
Downloads:<br>
<a href="http://mountainutilities.eu/bcmanager">BCRManager</a><br>
<a href="https://atom.io">Atom</a><br>
<br>
Based off FCB1020 scripts at <a href="http://remotescripts.blogspot.com">http://remotescripts.blogspot.com/</a><br>

<H4>Disclaimer</H4>
THESE FILES ARE PROVIDED AS-IS, WITHOUT ANY WARRANTY, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO FITNESS FOR ANY PARTICULAR PURPOSE.
