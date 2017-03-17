#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

import sys, traceback, time, Ice, IceStorm, getopt
from uuid import getnode as get_mac

Ice.loadSlice('Messagerie.ice')
import Central
class Publisher(Ice.Application):

    def run(self, args):
        try:
            opts, args = getopt.getopt(args[1:], '', ['datagram', 'twoway', 'oneway'])
        except getopt.GetoptError:
            self.usage()
            return 1

        
        optsSet = 0
        topicName = "MessagerieCentral"
        optsSet = optsSet + 1
        manager = IceStorm.TopicManagerPrx.checkedCast(self.communicator().propertyToProxy('TopicManager.Proxy'))
        if not manager:
            print(args[0] + ": invalid proxy")
            return 1

        #
        # Retrieve the topic.
        #
        try:
            topic = manager.retrieve(topicName)
        except IceStorm.NoSuchTopic:
            try:
                topic = manager.create(topicName)
            except IceStorm.TopicExists:
                print(self.appName() + ": temporary error. try again")
                return 1

        #
        # Get the topic's publisher object, and create a Clock proxy with
        # the mode specified as an argument of this application.
        #
        publisher = topic.getPublisher();
        publisher = publisher.ice_oneway();
        messagerie = Central.MessageriePrx.uncheckedCast(publisher)
        mac = get_mac()
        print("publishing tick events. Press ^C to terminate the application.")
        try:
            while 1:
                messagerie.notify(str(mac))
                time.sleep(1)
        except IOError:
            # Ignore
            pass
        except Ice.CommunicatorDestroyedException:
            # Ignore
            pass
                
        return 0

app = Publisher()
sys.exit(app.main(sys.argv, "config.pub"))
