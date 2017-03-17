# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `Interface.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module Music
_M_Music = Ice.openModule('Music')
__name__ = 'Music'

if '_t_song' not in _M_Music.__dict__:
    _M_Music._t_song = IcePy.defineSequence('::Music::song', (), IcePy._t_byte)

if '_t_liste' not in _M_Music.__dict__:
    _M_Music._t_liste = IcePy.defineSequence('::Music::liste', (), IcePy._t_string)

if 'mp3' not in _M_Music.__dict__:
    _M_Music.mp3 = Ice.createTempClass()
    class mp3(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_Music.mp3:
                raise RuntimeError('Music.mp3 is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Music::mp3')

        def ice_id(self, current=None):
            return '::Music::mp3'

        def ice_staticId():
            return '::Music::mp3'
        ice_staticId = staticmethod(ice_staticId)

        def findByName(self, nameSong, current=None):
            pass

        def findById(self, idSong, current=None):
            pass

        def add(self, theSong, nameSong, idSong, current=None):
            pass

        def delete(self, nameSong, current=None):
            pass

        def getALL(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Music._t_mp3)

        __repr__ = __str__

    _M_Music.mp3Prx = Ice.createTempClass()
    class mp3Prx(Ice.ObjectPrx):

        def findByName(self, nameSong, _ctx=None):
            return _M_Music.mp3._op_findByName.invoke(self, ((nameSong, ), _ctx))

        def begin_findByName(self, nameSong, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.mp3._op_findByName.begin(self, ((nameSong, ), _response, _ex, _sent, _ctx))

        def end_findByName(self, _r):
            return _M_Music.mp3._op_findByName.end(self, _r)

        def findById(self, idSong, _ctx=None):
            return _M_Music.mp3._op_findById.invoke(self, ((idSong, ), _ctx))

        def begin_findById(self, idSong, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.mp3._op_findById.begin(self, ((idSong, ), _response, _ex, _sent, _ctx))

        def end_findById(self, _r):
            return _M_Music.mp3._op_findById.end(self, _r)

        def add(self, theSong, nameSong, idSong, _ctx=None):
            return _M_Music.mp3._op_add.invoke(self, ((theSong, nameSong, idSong), _ctx))

        def begin_add(self, theSong, nameSong, idSong, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.mp3._op_add.begin(self, ((theSong, nameSong, idSong), _response, _ex, _sent, _ctx))

        def end_add(self, _r):
            return _M_Music.mp3._op_add.end(self, _r)

        def delete(self, nameSong, _ctx=None):
            return _M_Music.mp3._op_delete.invoke(self, ((nameSong, ), _ctx))

        def begin_delete(self, nameSong, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.mp3._op_delete.begin(self, ((nameSong, ), _response, _ex, _sent, _ctx))

        def end_delete(self, _r):
            return _M_Music.mp3._op_delete.end(self, _r)

        def getALL(self, _ctx=None):
            return _M_Music.mp3._op_getALL.invoke(self, ((), _ctx))

        def begin_getALL(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.mp3._op_getALL.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getALL(self, _r):
            return _M_Music.mp3._op_getALL.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Music.mp3Prx.ice_checkedCast(proxy, '::Music::mp3', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Music.mp3Prx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Music._t_mp3Prx = IcePy.defineProxy('::Music::mp3', mp3Prx)

    _M_Music._t_mp3 = IcePy.defineClass('::Music::mp3', mp3, -1, (), True, False, None, (), ())
    mp3._ice_type = _M_Music._t_mp3

    mp3._op_findByName = IcePy.Operation('findByName', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Music._t_song, False, 0), ())
    mp3._op_findById = IcePy.Operation('findById', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), _M_Music._t_song, False, 0), ())
    mp3._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Music._t_song, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    mp3._op_delete = IcePy.Operation('delete', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    mp3._op_getALL = IcePy.Operation('getALL', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Music._t_liste, False, 0), ())

    _M_Music.mp3 = mp3
    del mp3

    _M_Music.mp3Prx = mp3Prx
    del mp3Prx

if 'controle' not in _M_Music.__dict__:
    _M_Music.controle = Ice.createTempClass()
    class controle(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_Music.controle:
                raise RuntimeError('Music.controle is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Music::controle')

        def ice_id(self, current=None):
            return '::Music::controle'

        def ice_staticId():
            return '::Music::controle'
        ice_staticId = staticmethod(ice_staticId)

        def filter(self, theSong, current=None):
            pass

        def bass(self, theSong, level, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Music._t_controle)

        __repr__ = __str__

    _M_Music.controlePrx = Ice.createTempClass()
    class controlePrx(Ice.ObjectPrx):

        def filter(self, theSong, _ctx=None):
            return _M_Music.controle._op_filter.invoke(self, ((theSong, ), _ctx))

        def begin_filter(self, theSong, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.controle._op_filter.begin(self, ((theSong, ), _response, _ex, _sent, _ctx))

        def end_filter(self, _r):
            return _M_Music.controle._op_filter.end(self, _r)

        def bass(self, theSong, level, _ctx=None):
            return _M_Music.controle._op_bass.invoke(self, ((theSong, level), _ctx))

        def begin_bass(self, theSong, level, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Music.controle._op_bass.begin(self, ((theSong, level), _response, _ex, _sent, _ctx))

        def end_bass(self, _r):
            return _M_Music.controle._op_bass.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Music.controlePrx.ice_checkedCast(proxy, '::Music::controle', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Music.controlePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Music._t_controlePrx = IcePy.defineProxy('::Music::controle', controlePrx)

    _M_Music._t_controle = IcePy.defineClass('::Music::controle', controle, -1, (), True, False, None, (), ())
    controle._ice_type = _M_Music._t_controle

    controle._op_filter = IcePy.Operation('filter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Music._t_song, False, 0),), (), ((), _M_Music._t_song, False, 0), ())
    controle._op_bass = IcePy.Operation('bass', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Music._t_song, False, 0), ((), IcePy._t_int, False, 0)), (), ((), _M_Music._t_song, False, 0), ())

    _M_Music.controle = controle
    del controle

    _M_Music.controlePrx = controlePrx
    del controlePrx

# End of module Music
