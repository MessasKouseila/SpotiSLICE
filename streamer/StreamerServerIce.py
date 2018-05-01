#!/usr/bin/env python
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : class gerant le côté Ice du server de streaming, implémentations de l'interface Streamer
# et mise à disposition de l'object qui permet l'accès à ces fonctions
#########################################

import os, sys, traceback, glob, Ice
from threading import Thread
import time
Ice.loadSlice('../app.ice')
import appli
import signal



class StreamerI(appli.Streamer):

    def __init__(self, ipAdd, port):
        self.ip = ipAdd
        self.port = port
        self.url = self.ip+":"+"8080"+"/"
        self.album = []

    def addSong(self, music, nameSong, author, album, genre, current = None):
        return True



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
            object = StreamerI(self.ip, self.port)
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