#!/usr/bin/env python
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : Class Main du server Central, gere le côté Subscriber, Ice, appel des fonctions des server streamer 
#########################################
import sys, traceback, Ice, IceStorm, getopt
from threading import Thread
import time
import os
import subprocess
import signal
Ice.loadSlice('../Messagerie.ice')
import Central
from StreamerServer import StreamerServer
from CentralServerIce import CentralServerIce


class MessagerieI(Central.Messagerie):
    def __init__(self, central):
        self.central = central
    # un server de stream se conecte au serverCentral
    def inscription(self, addIp, port, current = None):
        print("inscription du server streamer\n ip : {0} \n port : {1} : ".format(addIp, port))
        element = StreamerServer(addIp, port)
        self.central.add(addIp, element)
        self.central.ALBUM[addIp] = self.central.Allstreamer[addIp].Streamer.getRepertoire()
        self.central.displaySong()

    # un server de stream se deconnecte du serverCentral
    def deconnexion(self, addIp, current = None):
        print("deconnexion du server streamer\n addIp : {0}".format(addIp))
        self.central.Allstreamer[addIp].stop() 
        self.central.Allstreamer.pop(addIp)
        self.central.ALBUM.pop(addIp)
    # reception d'une notification de la part du server de stream
    def notify(self, info, addIp, current = None):
        print("notification du server streamer {0}\n info : {1}".format(addIp, info))
        self.central.ALBUM[addIp] = self.central.Allstreamer[addIp].Streamer.getRepertoire()

# permet d'ecouter les messages reçu sur un topic, et d'executer des fonctions celon le message reçu
class CentralServerMain(Ice.Application):
    
    def __init__(self):
        self.Allstreamer = {}
        self.centralIce = CentralServerIce("127.0.0.1", "5000", self)
        self.ALBUM = {}
    def displaySong(self):
        for i in self.ALBUM.values():
            for j in i:
                print(j.name)
    def add(self, addIp, streamer):
        self.Allstreamer[addIp] = streamer

    # fonction qui lance le ServerCentral, gere les messages reçu depuis les servers Streamer
    # gere l'appel au fonctions des serveur de Stream
    def run(self, args):
        topicName = "MessagerieCentral"
        id = ""
        manager = IceStorm.TopicManagerPrx.checkedCast(self.communicator().propertyToProxy('TopicManager.Proxy'))
        if not manager:
            print("invalid proxy")
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

        subId = Ice.Identity()
        subId.name = id
        if len(subId.name) == 0:
            subId.name = Ice.generateUUID()
        subscriber = adapter.add(MessagerieI(self), subId)

        #
        # Activate the object adapter before subscribing.
        #
        adapter.activate()

        qos = {}
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
        self.centralIce.start()
        print("Central Server is running")
        while True:
            cmd = raw_input("x to terminate  :   ")
            if cmd == "x":
                self.centralIce.stop()
                for val in self.Allstreamer.values():
                    val.stop()
                topic.unsubscribe(subscriber)
                break 
        return 0

app = CentralServerMain()
app.main(sys.argv, "config.sub")