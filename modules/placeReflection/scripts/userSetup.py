# ----------------------------------------------------------------------
# userSetup.py
#
# Automatically add the menu item for the place reflection tool upon
# Maya startup.
#
# Copyright (c) 2018 Ingo Clemens, brave rabbit
# www.braverabbit.com
#
# Version: 1.2.4 (2018-10-14)
#
# ----------------------------------------------------------------------

from maya import cmds, mel, utils

def addMenuItem():
    if not cmds.about(batch=True):
        mel.eval("source brPlaceReflectionAddMenuItem; brPlaceReflectionAddMenuCommand;")

utils.executeDeferred(addMenuItem)

# ----------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2018 Ingo Clemens, brave rabbit
# placeReflection and quickZoom are under the terms of the MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Author: Ingo Clemens    www.braverabbit.com
# ----------------------------------------------------------------------
