# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from MIDI_Fighter_Twister import MIDI_Fighter_Twister

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return MIDI_Fighter_Twister(c_instance)


# local variables:
# tab-width: 4
