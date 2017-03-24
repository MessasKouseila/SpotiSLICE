#!/usr/bin/env python
# coding: utf8

import os, sys, traceback, time, Ice, IceStorm, getopt, socket
import threading
import subprocess
import signal
from uuid import getnode as get_mac
Ice.loadSlice('../Messagerie.ice')
import Central
from StreamerServerIce import StreamerServerIce

class StreamerMain(Ice.Application):
    def __init__(self, port="6000"):
        self.ip = self.getIp()
        self.port = port
        self.instance = StreamerServerIce(self.ip, self.port)
        self.ednaStart = None
    def getIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    def edna(self):
        f1 = 'startEdna.sh'
        self.ednaStart = subprocess.Popen(['bash', f1])
    def menu(self):
        print("\n======= MENU =======\n")
        print("Pour ajouter une music, ajouter au repertoire /music les musiques et appuyer sur 1 ")
        print("1 - mettre à jour")
        print("2 - deconnexion")
        return raw_input("Saisire  :  ")

    def update(self):
        print("mise a jour du sereur")

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
        try:
            messagerie.inscription(self.ip, self.port, str(mac))
            self.instance.start()
            t = threading.Thread(target=self.edna)
            t.start()
            print("Streamer is running on ip = {0}, port = {1}".format(self.ip, self.port))
            
            while True:
                choix = str(self.menu())
                if choix == "1":
                    self.update()
                else:
                    messagerie.deconnexion(self.ip)
                    self.ednaStart.kill()
                    f2 = 'stopEdna.sh'
                    stop = subprocess.Popen(['bash', f2])
                    time.sleep(2)
                    stop.kill()
                    self.instance.stop()
                    break
               
        except IOError:
            # Ignore
            pass
        except Ice.CommunicatorDestroyedException:
            # Ignore
            pass  
        return 0
        
app = StreamerMain()
sys.exit(app.main(sys.argv, "config.pub"))