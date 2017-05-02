#!/usr/bin/env python
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : Class Main du server Central, gere le côté Subscriber, Ice, appel des fonctions des server streamer 
#########################################

import os, sys, time, threading, subprocess, signal, socket
import traceback, Ice, IceStorm
Ice.loadSlice('../Messagerie.ice')
import Central
from CentralServerIce import CentralServerIce
from BddCentral import BddCentral

class MessagerieI(Central.Messagerie):
    def __init__(self, central):
        self.central = central
    # un server de stream se conecte au serverCentral
    def refresh(self, addIp, current = None):
        self.central.Allstreamer[addIp] = True
        
    def delFromRep(self, addIp, Rep, current = None):
        self.central.Allstreamer[addIp] = True
        print("suppression des musiques suivantes : \n")
        for i in Rep:
            self.central.bdd.deleteByName(i.name, addIp)
            print(i.name + "\n")

    def addToRep(self, addIp, Rep, current = None):
        self.central.Allstreamer[addIp] = True
        print("ajout des musiques suivantes : \n")
        for i in Rep:
            self.central.bdd.add(i, addIp)
            print(i.name + "\n")

    def sendAlbum(self, addIp, Rep, current = None):
        print("inscription du server streamer\n ip : {0} : ".format(addIp))
        self.central.Allstreamer[addIp] = True
        for i in Rep:
            self.central.bdd.add(i, addIp)
            print(i.name)

    # un server de stream se deconnecte du serverCentral
    def deconnexion(self, addIp, current = None):
        print("deconnexion du server streamer\n addIp : {0}".format(addIp))
        self.central.Allstreamer.pop(addIp)
        self.central.bdd.deleteByIp(addIp)

    # reception d'une notification de la part du server de stream
    def notify(self, info, addIp, current = None):
        print("notification du server streamer {0}\n info : {1}".format(addIp, info))
        

# permet d'ecouter les messages reçu sur un topic, et d'executer des fonctions celon le message reçu
class CentralServerMain(Ice.Application):
    
    def __init__(self):
        # addIP (StreamerServer) ==> bool, true ServerStreamer is connected, false,it is deconnected (Delete it from de rep)
        self.Allstreamer = {}
        ip = self.getIp()
        self.centralIce = CentralServerIce(ip, "5000", self)
        self.bdd = BddCentral()
        self.bdd.createDB()
        self.bdd.deleteAll()
        # on verifie que les serverStreamer sont toujours disponible, on faisant un check sur l'envoie de notifcation
        # chaque serverStreamer doit nous notifier d'un message pour qu'on puisse le considerer comme etant toujours disponible
        self.threadCheker = threading.Thread(target=self.checkValidite, args=(180,))
        self.tChek = True
    # verifie que les serveur de streamer on envoyé un message pour notifié de leurs activités.
    # si la valeur est à false, alors le streamer et toute sa musique est supprimer de la bdd centrale
    def checkValidite(self, timOut):
        while self.tChek:
            time.sleep(5)
            time.sleep(timOut)
            for cle, valeur in self.Allstreamer.items():
                if (not valeur):
                    self.Allstreamer.pop(cle)
                    self.bdd.deleteByIp(cle)
                else:
                    self.Allstreamer[cle] = False                  
    # ajout d'une musique dans la bdd centrale
    def addMusic(self, addIp, music):
        self.bdd.add(music, addIp)
    # suppression d'une musique dans la bdd centrale
    def delMusic(self, addIp, music):
        self.bdd.deleteByName(music.name, addIp)
    # renvoie la liste de toutes les musiques disponibles.
    def getAllbum(self):
        return self.bdd.findAll()
    # renvoie l'ip sur lequel est executé le scripte, dans mon cas renvoie l'ip de mon serveur centrale 
    def getIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip = s.getsockname()[0]
        s.close()
        return ip

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
        # configuration de la connexion au depot
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
        subscriber = subscriber.ice_oneway()
        try:
            topic.subscribeAndGetPublisher(qos, subscriber)
        except IceStorm.AlreadySubscribed as ex:
            if len(id) == 0:
                raise
            print("reactivating persistent subscriber")
        
        self.shutdownOnInterrupt()
        self.centralIce.start()
        self.threadCheker.start()
        print("Central Server is running \n")
        while True:
            cmd = raw_input("x to terminate  :   \n")
            # taper x sur le clavier afin d'arreté le serveur centrale
            if cmd == "x":
                self.centralIce.stop()
                topic.unsubscribe(subscriber)
                self.tChek = False
                f2 = "stop.sh"
                # on lance un script qui stope toutes les activités du serveur central
                stop = subprocess.Popen(['bash', f2, "CentralServerMain.py"])
                time.sleep(1)
                stop.kill()
                break 
        return 0

app = CentralServerMain()
app.main(sys.argv, "config.sub")