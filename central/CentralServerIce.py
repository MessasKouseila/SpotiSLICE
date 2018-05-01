#!/usr/bin/env python
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : Class gérant le côté Ice du server central,
# met à disposition des clients android un object pour qu'ils puissent avoir accès à ces méthodes 
#########################################

import sys, traceback, Ice
from threading import Thread
import time
Ice.loadSlice('../app.ice')
import appli

class CentralI(appli.Central):
    def __init__(self, iceCentral = None):
        self.Central = iceCentral
    # renvoie la liste des musiques correspendant au nom donnée en paramètre
    def findByName(self, nameSong, current = None):
        print("findByName")
        return self.Central.bdd.findByName(nameSong)

    def findByAuth(self, nameAuthor, current = None):
        print("findByAuth")
        return self.Central.bdd.findByAuth(nameAuthor)

    def findByAlbum(self, nameAlbum, current = None):
        print("findByAlbum")
        return self.Central.bdd.findByAlbum(nameAlbum)

    def findByGenre(self, nameGenre, current = None):
        print("findByGenre")                        
        return self.Central.bdd.findByGenre(nameGenre)

    def getAllAvailableSong(self, current = None):
        print("getAllAvailableSong est appele par le client")
        return self.Central.bdd.findAll()



    def getStreamer(self, current = None):
        print("return a streamer to client to add a music")


        
# met à disposition un objet permettant d'exectuer des fonction coté CentralServer            
class CentralServerIce(Thread):
    # ip et port ou on peut accedé au fonctions du CentralServer
    def __init__(self, addip="127.0.0.1", port="5000", instOfCentral=None):
        Thread.__init__(self)
        self.ip = addip
        self.port = port
        # nom de l'adaptateur
        self.nameAdp = "Central"
        self.ic = None
        self.adapteur = None
        self.iceCentral = instOfCentral

    def run(self):
        print("lancement du Ice côté Central")
        arg = "tcp -h "+self.ip+" -p "+self.port
        try:
            self.ic = Ice.initialize(sys.argv)
            self.adapter = self.ic.createObjectAdapterWithEndpoints(self.nameAdp, arg)
            object = CentralI(self.iceCentral)
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
            