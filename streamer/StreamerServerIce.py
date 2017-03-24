#!/usr/bin/env python
# coding: utf8
import os, sys, traceback, Ice
from threading import Thread
import time
Ice.loadSlice('../app.ice')
import appli
import signal

class StreamerI(appli.Streamer):
    def getRepertoire(self, current = None):
        return "ceci est un test"
    def addSong(self, music, nameSong, current = None):
        return True
    def checkStream(self, nameSong, current=None):
        return None


class StreamerServerIce(Thread):
    # ip et port ou on peut accedé au fonctions du server de stream
    def __init__(self, addip="127.0.0.1", port="6000"):
        Thread.__init__(self)
        self.ip = addip
        self.port = port
        # nom de l'adaptateur
        self.adapteur = "Central"
        self.ic = None

    def run(self):
        arg = "tcp -h "+self.ip+" -p "+self.port
        try:
            self.ic = Ice.initialize(sys.argv)
            adapter = self.ic.createObjectAdapterWithEndpoints(self.adapteur, arg)
            object = StreamerI()
            adapter.add(object, self.ic.stringToIdentity(self.adapteur))
            adapter.activate()
            #self.ic.waitForShutdown()
        except:
            traceback.print_exc()
            status = 1

    def stop(self):
        self.ic.shutdown()
        if self.ic:
            # Clean up
            try:
                self.ic.destroy()
            except:
                traceback.print_exc()