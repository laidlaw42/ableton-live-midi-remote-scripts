Contents: Scripts for creating custom MIDI Remote Scripts for Ableton Live.
(Known) Working versions: 9.2 and above (currently 9.7.1)

<a href="https://youtu.be/IgKwcCJsoz4">In-depth video tutorial</a>
For the Push 2, user <a href="https://github.com/jzgdev/Push2UserModeScript">jzgdev</a> has a working Push 2 User Mode.


Additional:
To change the size of the track selection box (coloured box in Session view),
Open “YourControllerName.py”

Change the values in the brackets () of lines 94, 99, 100, 106 and 107 to suit your needs

On line 94 the first number is the amount horizontally and second is vertical.
Lines 99 and 106 are vertical, 100 and 112 are horizontal. 
Make sure the value that you input corresponds with the two values on line 94. 


This is what the code will look like:
94        self._session = SpecialSessionComponent(X, Y)
99        self._scene_launch_buttons = [self._note_map[SCENELAUNCH[index]] for index in range(X) ]
100       self._track_stop_buttons = [self._note_map[TRACKSTOP[index]] for index in range(Y) ]
106       for scene_index in range(X):
112       for track_index in range(Y):

Lastly, don’t forget to add or remove rows/columns for SCENELAUNCH and CLIPNOTEMAP from MIDI_Map.py


Downloads:
<a href="http://mountainutilities.eu/bcmanager">BCRManager</a>
<a href="https://atom.io">Atom</a>

Based off FCB1020 scripts at <a href="http://remotescripts.blogspot.com">http://remotescripts.blogspot.com/</a>

<H4>Disclaimer</H4>
THESE FILES ARE PROVIDED AS-IS, WITHOUT ANY WARRANTY, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO FITNESS FOR ANY PARTICULAR PURPOSE.
