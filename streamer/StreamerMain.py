#!/usr/bin/env python
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : class Main du server de streaming
# http://192.168.2.130:8080
#########################################

import os, sys, glob, traceback, time, Ice, IceStorm, getopt, socket
import threading
import subprocess
import signal
Ice.loadSlice('../Messagerie.ice')
import Central
from StreamerServerIce import StreamerServerIce

class StreamerMain(Ice.Application):
    def __init__(self, port="6000"):
        self.ip = self.getIp()
        self.port = port
        # self.instance = StreamerServerIce(self.ip, self.port)
        self.ednaStart = None
        self.url = self.ip+":"+"8080"+"/"
        self.album = []
        self.tRep = True
        self.tRefresh = True 

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
        print("ajout/supression de music via le repertoire\n")
        print("1 - mettre à jour\n")
        print("2 - deconnexion\n")
        return raw_input("Saisire  :  ")
     
    def getRepertoir(self):
        # on recupere le repertoir courrant
        current_directory = os.getcwd()
        # on recupere le chemin absolu du fichier de configuration
        file_album = current_directory + "/album/"
        # on cherche les musiques
        listmyalbum = file_album + "*.mp3"
        tmp_album = []
        for i in glob.glob(listmyalbum):
            j = i.split("/")
            tmp_album.append(Central.music(j[len(j)- 1], self.url+j[len(j)- 1]))
        return tmp_album

    def sendAlb(self, messagerie):
        self.album = self.getRepertoir()
        for i in self.album:
            print(i.name + " " + i.url)
        messagerie.sendAlbum(self.ip, self.album)

    def threadRep(self, messagerie):
        while self.tRep:
            time.sleep(60)
            self.refreshMyRep(messagerie)

    def refreshMyRep(self, messagerie):
        new_album = self.getRepertoir()  
        tmp = []
        # nouvelle musique ajouter, en notify le Central
        if (len(new_album) > len(self.album)):
            for i in new_album:
                if (self.album.count(i) == 0):
                    tmp.append(i)
                    self.album.append(i)
            if (len(tmp) != 0):
                messagerie.addToRep(self.ip, tmp)
                print("ajout des musiques suivantes : \n")
                for i in tmp:
                    print(i.name + "\n")

        elif (len(new_album) < len(self.album)):
            for i in self.album:
                if (new_album.count(i) == 0):
                    tmp.append(i)
                    self.album.remove(i)
            if (len(tmp) != 0):
                messagerie.delFromRep(self.ip, tmp) 
                print("suppression des musiques suivantes : \n")
                for i in tmp:
                    print(i.name + "\n")
        else:
            print("aucune mise a jour !!!!!!!!!!!")                                     
            

    def sendRefresh(self, messagerie):
        while self.tRefresh:
            time.sleep(180)
            messagerie.refresh(self.ip)                 

    def run(self, args):
        # self.instance.start()
        t = threading.Thread(target=self.edna)
        t.start()
        topicName = "MessagerieCentral"
        manager = IceStorm.TopicManagerPrx.checkedCast(self.communicator().propertyToProxy('TopicManager.Proxy'))
        if not manager:
            print("invalid proxy")
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
 
        try:

            self.sendAlb(messagerie)
            refreshThread = threading.Thread(target=self.sendRefresh, args=(messagerie, ))
            refreshThread.start()
            repThread = threading.Thread(target=self.threadRep, args=(messagerie, ))
            repThread.start()
            print("Streamer is running on ip = {0}, port = {1}".format(self.ip, self.port))
            
            while True:
                choix = str(self.menu())
                if choix == "1": 
                    print("mise a jour de l'album")
                    messagerie.notify("album mis à jour", self.ip)
                    self.refreshMyRep(messagerie)
                elif choix == "2":
                    messagerie.deconnexion(str(self.ip))
                    self.ednaStart.kill()
                    f2 = 'stop.sh'
                    stop = subprocess.Popen(['bash', f2, "edna.py"])
                    time.sleep(1)
                    stop.kill()
                    self.tRefresh = False
                    self.tRep = False
                    stop = subprocess.Popen(['bash', f2, "StreamerMain.py"])
                    time.sleep(1)
                    stop.kill()
                    #self.instance.stop()
                    break   
                else:
                    print("Erreur de saisie")               
        except IOError:
            # Ignore
            pass
        except Ice.CommunicatorDestroyedException:
            # Ignore
            pass  
        return 0
        
app = StreamerMain()
sys.exit(app.main(sys.argv, "config.pub"))