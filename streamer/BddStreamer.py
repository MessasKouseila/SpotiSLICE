#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3, os, sys, time, Ice, traceback
from datetime import date, datetime
Ice.loadSlice('../app.ice')
import appli
class BddStreamer():
    # ip et port ou on peut accedé au fonctions du CentralServer
    def __init__(self):
        # on sauvegarde le chemun absolu pour acceder à la base de donnees
        tmp = os.getcwd()
        self.PATH = tmp + "/localDB.db"
        self.dbMusic = None

    def createDB(self):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            # Table des musics
            curseur.execute("""
            CREATE TABLE IF NOT EXISTS music_streamer(
                id_music INTEGER PRIMARY KEY,
                date_insert DATE,
                name VARCHAR(50),
                author VARCHAR(50),
                album VARCHAR(50),
                genre VARCHAR(50),
                url VARCHAR(100)
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

    def add(self, music):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
            "SELECT COALESCE(MAX(id_music), 0) FROM music_streamer")
        id_music = curseur.fetchone()[0] + 1
        date_insert = date.today()
        curseur.execute(
            "INSERT INTO music_streamer VALUES (?, ?, ?, ?, ?, ?, ?)", (id_music, date_insert, music.name, music.author, music.album, music.genre, music.url))
        self.dbMusic.commit()
        self.dbMusic.close()
    # Return list of all music as object
    # 
               
    def findAll(self):
        
        self.dbMusic = sqlite3.connect(self.PATH)
        curseur = self.dbMusic.cursor()
        curseur.execute(
            "SELECT * FROM music_streamer")
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
           "SELECT * FROM music_streamer WHERE name = ?", (nameSong, ))
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
                "DELETE FROM music_streamer")
            self.dbMusic.commit()             
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()
    def deleteByName(self, nameSong):
        try:
            self.dbMusic = sqlite3.connect(self.PATH)
            curseur = self.dbMusic.cursor()
            curseur.execute(
                "DELETE FROM music_streamer WHERE name = ?", (nameSong, ))
            self.dbMusic.commit()             
        except Exception as e:
            # Roll back si il y a des erreurs
            self.dbMusic.rollback()
            raise e
        finally:
            # fermer la bdd
            self.dbMusic.close()         