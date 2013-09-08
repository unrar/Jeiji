#!/usr/bin/env python

### Utils for both the developer and user of Jeiji.

# Some colors
class Colors:
    ### This is the line that you want to edit
    ### Replace False with True to enable colors!
    def __init__(self, falfo = False):
        if falfo:
            self.red = "\033[01;31m{0}\033[00m"
            self.green = "\033[1;36m{0}\033[00m"
            self.blue = "\033[1;34m{0}\033[00m"
        else:
            self.red = "{0}"
            self.green = "{0}"
            self.blue = "{0}"

##
