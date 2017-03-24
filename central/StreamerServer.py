#!/usr/bin/env python
# coding: utf8  

import os, sys, time, traceback, Ice
from multiprocessing.pool import ThreadPool
Ice.loadSlice('../app.ice')
import appli

class StreamerServer():
    def __init__(self, addip="127.0.0.1", port="5000"):
        self.ip = addip
        self.port = port
        # nom de l'adaptateur
        self.adapteur = "Central"
        self.arg = ":tcp -h "+self.ip+" -p "+self.port
        self.ic = None
        self.base = None
        self.Streamer = None
        try:
            self.ic = Ice.initialize(sys.argv)
            self.base = self.ic.stringToProxy(self.adapteur+self.arg)
            self.Streamer = appli.StreamerPrx.checkedCast(self.base)
            if not self.Streamer:
                raise RuntimeError("Invalid proxy")
        except:
            traceback.print_exc()
    def stop(self):
        self.ic.shutdown()
        if self.ic:
            # Clean up
            try:
                self.ic.destroy()
            except:
                traceback.print_exc()               