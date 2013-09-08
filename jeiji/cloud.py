#!/usr/bin/env python
from utils import Colors

#########
# Cloud #
#########

# This class must be passed to Jeiji. It describes your cloud.
class Cloud:
    ## Constructor
    def __init__(self):
        cc = Colors()
        print(cc.blue.format("[INFO] Cloud reference created. Waiting for description..."))
        self.described = False

    ## Describe the cloud
    def describe(self, type, url, port, username, password):
        self.type = type
        self.url = url
        self.port = str(port)
        self.username = username
        self.password = password
        self.described = True
        cc = Colors()
        print(cc.green.format("[INFO] Cloud properly described!"))
    