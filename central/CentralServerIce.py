#!/usr/bin/env python
# coding: utf8


import sys, traceback, Ice
from threading import Thread
import time
Ice.loadSlice('../app.ice')
import appli
class CentralI(appli.Central):
    # inscription d'un client au Central
    def inscriptionClient(self, login, passWord, current = None):
        print("inscription du client")
    # connexion d'un client au serveur Central
    def connectionClient(slef, login, passWord, current = None):
        print("connection du client")
    # renvoie la liste des musiques correspendant au nom donnée en paramètre
    def findByName(slef, nameSong, current = None):
        print("findByName")
    # lance le streamCentralServing de la musique choisie par le client
    def streamByName(slef, nameSong, current = None):
        print("streamByName")
    def add(slef, theSong, nameSong, current = None):
        print("add")
    def getAllAvailableSong(slef, current = None):
        print("getAllAvailableSong")
        
# met à disposition un objet permettant d'exectuer des fonction coté CentralServer            
class CentralServerIce(Thread):
    # ip et port ou on peut accedé au fonctions du CentralServer
    def __init__(self, addip="127.0.0.1", port="5000"):
        Thread.__init__(self)
        self.ip = addip
        self.port = port
        # nom de l'adaptateur
        self.nameAdp = "Central"
        self.ic = None
        self.adapteur = None

    def run(self):
        arg = "tcp -h "+self.ip+" -p "+self.port
        try:
            self.ic = Ice.initialize(sys.argv)
            self.adapter = self.ic.createObjectAdapterWithEndpoints(self.nameAdp, arg)
            object = CentralI()
            self.adapter.add(object, self.ic.stringToIdentity(self.nameAdp))
            self.adapter.activate()
        except:
            traceback.print_exc()
            status = 1
    def stop(self):          
        if self.ic:
            # Clean up
            try:
                self.ic.destroy()
            except:
                traceback.print_exc()
            