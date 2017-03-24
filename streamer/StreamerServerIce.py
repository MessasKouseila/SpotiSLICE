#!/usr/bin/env python
# coding: utf8
import os, sys, traceback, Ice
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

    def getRepertoire(self, current = None):
        # on recupere le repertoir courrant
        current_directory = os.getcwd()
        # on recupere le chemin absolu du fichier de configuration
        file_album = current_directory + "/album/"
        # on cherche les musiques
        listmyalbum = file_album + "*.mp3"
        for i in glob.glob(listmyalbum):
            j = i.split("/")
            self.album.append(Music(j[len(j)- 1], self.url+j[len(j)- 1]))
        return self.album

    def addSong(self, music, nameSong, current = None):
        return True
        
    # verifie que la music est disponible au stream    
    def checkStream(self, nameSong, current=None):
        if self.contains(nameSong):
            return True
        else:
            return False
    # cherche la music dans le l'album, renvoie True si elle existe
    def contains(self, name):
        for i in self.album:
            if i.name == name:
                return True
        return False        



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