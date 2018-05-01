#!/usr/bin/env python3
# coding: utf8
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : permet la création et la gestion de la base de donnée central de l'apllication, utilisé par le serveur central.  
#########################################

import sqlite3, os, sys, time, traceback, Ice
from datetime import date, datetime
Ice.loadSlice('../app.ice')
import appli

class BddCentral():
    # ip et port ou on peut accedé au fonctions du CentralServer
    def __init__(self):
        # on sauvegarde le chemun absolu pour acceder a la base de donnees
        tmp = os.getcwd()
        self.PATH = tmp + "/Moteur_stockage.db"
        self.dbMusic = None
        # creation de la bdd
    def createDB(self):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            # Table des musics
            curseur.execute("""
            CREATE TABLE IF NOT EXISTS music(
                id_music INTEGER PRIMARY KEY,
                date_insert DATE,
                name COLLATE NOCASE,
                author COLLATE NOCASE,
                album COLLATE NOCASE,
                genre COLLATE NOCASE,
                url COLLATE NOCASE,
                addIp COLLATE NOCASE
            )
            """)
            self.dbMusic.commit()
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()
            
    # ajout d'une musique
    def add(self, music, addIp):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
            "SELECT COALESCE(MAX(id_music), 0) FROM music")
        id_music = curseur.fetchone()[0] + 1
        date_insert = date.today()
        curseur.execute(
            "INSERT INTO music VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id_music, date_insert, music.name, music.author, music.album, music.genre, music.url, addIp))
        self.dbMusic.commit()
        self.dbMusic.close()    
    # Retourne une liste de toutes les musiques disponible           
    def findAll(self):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
            "SELECT * FROM music")
        all_music = curseur.fetchall()
        res = []
        self.dbMusic.close()
        for i in all_music:
            res.append(appli.music(i[2], i[3], i[4], i[5], i[6]))
        return res

    # Retourne une liste de toutes ayant le même nom que le parametre  
    def findByName(self, nameSong):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
           "SELECT * FROM music WHERE name LIKE ?",(nameSong, ))
        all_music = curseur.fetchall()
        res = []
        self.dbMusic.close()
        for i in all_music:
            res.append(appli.music(i[2], i[3], i[4], i[5], i[6]))
        return res
    # Retourne une liste de toutes les musiques ayant comme auteur nameAuthor  
    def findByAuth(self, nameAuthor):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
           "SELECT * FROM music WHERE author LIKE ?",(nameAuthor, ))
        all_music = curseur.fetchall()
        res = []
        self.dbMusic.close()
        for i in all_music:
            res.append(appli.music(i[2], i[3], i[4], i[5], i[6]))
        return res

    # Retourne une liste de toutes les musiques comprise dans l'album nameAlbum
    def findByAlbum(self, nameAlbum):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
           "SELECT * FROM music WHERE album LIKE ?", (nameAlbum, ))
        all_music = curseur.fetchall()
        res = []
        self.dbMusic.close()
        for i in all_music:
            res.append(appli.music(i[2], i[3], i[4], i[5], i[6]))
        return res

    # Retourne une liste de toutes les musiques ayant comme Genre nameGenre
    def findByGenre(self, nameGenre):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
           "SELECT * FROM music WHERE genre LIKE ?",(nameGenre, ))
        all_music = curseur.fetchall()
        res = []
        self.dbMusic.close()
        for i in all_music:
            res.append(appli.music(i[2], i[3], i[4], i[5], i[6]))
        return res


    # vide toutes la bdd
    def deleteAll(self):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            curseur.execute(
                "DELETE FROM music")
            self.dbMusic.commit()             
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()
    # supprime la musique ayant comme nom nameSong, addIp étant l'identifiant du serveur de streaming contenant la musique.
    def deleteByName(self, nameSong, addIp):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            curseur.execute(
                "DELETE FROM music WHERE name =:name AND addIp=:addip", {"name":nameSong , "addip":addIp})
            self.dbMusic.commit()             
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()
    # supprime toutes les musiques heberger par le serveur de streaming ayant comme ip addIp        
    def deleteByIp(self, addIp):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            curseur.execute(
                "DELETE FROM music WHERE addIp = ?", (addIp, ))
            self.dbMusic.commit()             
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()         
bd = BddCentral()
bd.createDB()            