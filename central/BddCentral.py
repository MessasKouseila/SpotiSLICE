#!/usr/bin/env python3
# coding: utf8
import sqlite3, os, sys, time, Ice, traceback
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
    # Return list of all music as object            
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

    # Return list of music as object
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