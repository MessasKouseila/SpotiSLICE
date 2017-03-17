#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

import sys, traceback, Ice, IceStorm, getopt
Ice.loadSlice('Messagerie.ice')
import Central

class MessagerieI(Central.Messagerie):
    def inscription(self, addIp, port, addMac, current = None):
        print("inscription du server streamer\n ip : {0} \n port : {1} \n addMac : {2}".format(addIp, port, addMac))
    def deconnexion(self, addMac, current = None):
        print("deconnexion du server streamer\n addMac : {0}".format(addMac))  
    def notify(self, info, current = None):
        print("notification du server streamer\n info : {0}".format(info))

class Subscriber(Ice.Application):

    def run(self, args):
        try:
            opts, args = getopt.getopt(args[1:], '', ['datagram', 'twoway', 'oneway', 'ordered', 'batch',
                    'retryCount=', 'id='])
        except getopt.GetoptError:
            self.usage()
            return 1

        batch = False
        option = "None"
        topicName = "MessagerieCentral"
        id = ""
        retryCount = ""

        manager = IceStorm.TopicManagerPrx.checkedCast(self.communicator().propertyToProxy('TopicManager.Proxy'))
        if not manager:
            print(args[0] + ": invalid proxy")
            return 1

        #
        # Retrieve the topic.
        #
        try:
            topic = manager.retrieve(topicName)
        except IceStorm.NoSuchTopic as e:
            try:
                topic = manager.create(topicName)
            except IceStorm.TopicExists as ex:
                print(self.appName() + ": temporary error. try again")
                return 1

        adapter = self.communicator().createObjectAdapter("Messagerie.Subscriber")

        #
        # Add a servant for the Ice object. If --id is used the identity
        # comes from the command line, otherwise a UUID is used.
        #
        # id is not directly altered since it is used below to detect
        # whether subscribeAndGetPublisher can raise AlreadySubscribed.
        #

        subId = Ice.Identity()
        subId.name = id
        if len(subId.name) == 0:
            subId.name = Ice.generateUUID()
        subscriber = adapter.add(MessagerieI(), subId)

        #
        # Activate the object adapter before subscribing.
        #
        adapter.activate()

        qos = {}
        if len(retryCount) > 0:
            qos["retryCount"] = retryCount

        #
        # Set up the proxy.
        #

        subscriber = subscriber.ice_oneway()

        try:
            topic.subscribeAndGetPublisher(qos, subscriber)
        except IceStorm.AlreadySubscribed as ex:
            # If we're manually setting the subscriber id ignore.
            if len(id) == 0:
                raise
            print("reactivating persistent subscriber")

        self.shutdownOnInterrupt()
        self.communicator().waitForShutdown()

        #
        # Unsubscribe all subscribed objects.
        #
        topic.unsubscribe(subscriber)

        return 0

app = Subscriber()
sys.exit(app.main(sys.argv, "config.sub"))
