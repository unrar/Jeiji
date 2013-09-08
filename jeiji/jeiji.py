#!/usr/bin/env python

#########################################
#            Jeiji Cloud Manager        #
#########################################

from cloud import Cloud
import re
from utils import Colors
    
###########################################
# Start maanging the cloud                #
###########################################

class Jeiji:

    ### Constructor [needs: instance]
    def __init__(self, instance):
        # Create color manager
        self.cc = Colors()
        # If it's a cloud object
        if isinstance(instance, Cloud):
            self.ref = instance
        #If it's not:
        else:
            self.ref = False
            print(self.cc.red.format("Debug: A Jeiji object can only be used passing a Cloud object instance."))

    ## Analyze the cloud
    def analyze(self):
        # If the given cloud was valid
        if self.ref:
            # Not described yet
            if not self.ref.described:
                print(self.cc.red.format("[ERROR] Cloud isn't described yet."))
            else:
                print("")
                ## If it's an amazon cloud
                if re.search("Amazon", self.ref.type) or re.search("EC2", self.ref.type):
                    print(self.cc.green.format("Cloud type") + ": Amazon [ID: %s]" % self.ref.type)
                    # Full URL
                    print("Jeji URL: " + self.cc.blue.format("https://cloud.jeiji.io/gate/amazon ") + self.ref.port + " " + self.ref.username)
                    # Amazon URL
                    print("Vendor URL: " + self.cc.blue.format(self.ref.url + ":" + self.ref.port) + " " + self.ref.username)
                    # SHA256 Password
                    print("Password (SHA256): " + self.cc.green.format(self.ref.password))
                ## If it's a MS Windows Azure cloud
                elif re.search(r"Azure", self.ref.type):
                    print(self.cc.green.format("Cloud type") + ": Windows Azure [ID: %s]" % self.ref.type)
                    # Full URL
                    print("Jeji URL: " + self.cc.blue.format("https://cloud.jeiji.io/gate/azure ") + self.ref.port + " " + self.ref.username)
                    # Vendor URL
                    print("Vendor URL: " + self.cc.blue.format(self.ref.url + ":" + self.ref.port) + " " + self.ref.username)
                    # SHA256 Password
                    print("Password (SHA256): " + self.cc.green.format(self.ref.password))

                ## If it's Heroku
                elif re.search("Heroku", self.ref.type):
                    print(self.cc.green.format("Cloud type") + ": Heroku [ID: %s]" % self.ref.type)
                    # Full URL
                    print("Jeji URL: " + self.cc.blue.format("https://cloud.jeiji.io/gate/heroku ") + self.ref.port + " " + self.ref.username)
                    # Vendor URL
                    print("Vendor URL: " + self.cc.blue.format(self.ref.url + ":" + self.ref.port) + " " + self.ref.username)
                    # SHA256 Password
                    print("Password (SHA256): " + self.cc.green.format(self.ref.password))
                ## If it's another type
                else:
                    print(self.cc.green.format("Cloud type") + ": Other [ID: %s]" % self.ref.type)
                    # Full URL
                    print("Jeji URL: " + self.cc.red.format("None") + ". No JeijiFirewall provided for unknown clouds.")
                    # Vendor URL
                    print("Vendor URL: " + self.cc.blue.format(self.ref.url + ":" + self.ref.port) + " " + self.ref.username)
                    # SHA256 Password
                    print("Password (SHA256): " + self.cc.green.format(self.ref.password))



    
    
