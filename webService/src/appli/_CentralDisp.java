// **********************************************************************
//
// Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.6.3
//
// <auto-generated>
//
// Generated from file `app.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package appli;

public abstract class _CentralDisp extends Ice.ObjectImpl implements Central
{
    protected void
    ice_copyStateFrom(Ice.Object __obj)
        throws java.lang.CloneNotSupportedException
    {
        throw new java.lang.CloneNotSupportedException();
    }

    public static final String[] __ids =
    {
        "::Ice::Object",
        "::appli::Central"
    };

    public boolean ice_isA(String s)
    {
        return java.util.Arrays.binarySearch(__ids, s) >= 0;
    }

    public boolean ice_isA(String s, Ice.Current __current)
    {
        return java.util.Arrays.binarySearch(__ids, s) >= 0;
    }

    public String[] ice_ids()
    {
        return __ids;
    }

    public String[] ice_ids(Ice.Current __current)
    {
        return __ids;
    }

    public String ice_id()
    {
        return __ids[1];
    }

    public String ice_id(Ice.Current __current)
    {
        return __ids[1];
    }

    public static String ice_staticId()
    {
        return __ids[1];
    }

    public final boolean add(byte[] theSong, String nameSong)
    {
        return add(theSong, nameSong, null);
    }

    public final boolean connectionClient(String login, String passWord)
    {
        return connectionClient(login, passWord, null);
    }

    public final String[] findByName(String nameSong)
    {
        return findByName(nameSong, null);
    }

    public final String[] getAllAvailableSong()
    {
        return getAllAvailableSong(null);
    }

    public final boolean inscriptionClient(String login, String passWord)
    {
        return inscriptionClient(login, passWord, null);
    }

    public final String streamByName(String nameSong)
    {
        return streamByName(nameSong, null);
    }

    public static Ice.DispatchStatus ___inscriptionClient(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        IceInternal.BasicStream __is = __inS.startReadParams();
        String login;
        String passWord;
        login = __is.readString();
        passWord = __is.readString();
        __inS.endReadParams();
        boolean __ret = __obj.inscriptionClient(login, passWord, __current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        __os.writeBool(__ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    public static Ice.DispatchStatus ___connectionClient(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        IceInternal.BasicStream __is = __inS.startReadParams();
        String login;
        String passWord;
        login = __is.readString();
        passWord = __is.readString();
        __inS.endReadParams();
        boolean __ret = __obj.connectionClient(login, passWord, __current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        __os.writeBool(__ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    public static Ice.DispatchStatus ___findByName(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        IceInternal.BasicStream __is = __inS.startReadParams();
        String nameSong;
        nameSong = __is.readString();
        __inS.endReadParams();
        String[] __ret = __obj.findByName(nameSong, __current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        listeHelper.write(__os, __ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    public static Ice.DispatchStatus ___streamByName(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        IceInternal.BasicStream __is = __inS.startReadParams();
        String nameSong;
        nameSong = __is.readString();
        __inS.endReadParams();
        String __ret = __obj.streamByName(nameSong, __current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        __os.writeString(__ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    public static Ice.DispatchStatus ___add(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        IceInternal.BasicStream __is = __inS.startReadParams();
        byte[] theSong;
        String nameSong;
        theSong = songHelper.read(__is);
        nameSong = __is.readString();
        __inS.endReadParams();
        boolean __ret = __obj.add(theSong, nameSong, __current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        __os.writeBool(__ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    public static Ice.DispatchStatus ___getAllAvailableSong(Central __obj, IceInternal.Incoming __inS, Ice.Current __current)
    {
        __checkMode(Ice.OperationMode.Normal, __current.mode);
        __inS.readEmptyParams();
        String[] __ret = __obj.getAllAvailableSong(__current);
        IceInternal.BasicStream __os = __inS.__startWriteParams(Ice.FormatType.DefaultFormat);
        listeHelper.write(__os, __ret);
        __inS.__endWriteParams(true);
        return Ice.DispatchStatus.DispatchOK;
    }

    private final static String[] __all =
    {
        "add",
        "connectionClient",
        "findByName",
        "getAllAvailableSong",
        "ice_id",
        "ice_ids",
        "ice_isA",
        "ice_ping",
        "inscriptionClient",
        "streamByName"
    };

    public Ice.DispatchStatus __dispatch(IceInternal.Incoming in, Ice.Current __current)
    {
        int pos = java.util.Arrays.binarySearch(__all, __current.operation);
        if(pos < 0)
        {
            throw new Ice.OperationNotExistException(__current.id, __current.facet, __current.operation);
        }

        switch(pos)
        {
            case 0:
            {
                return ___add(this, in, __current);
            }
            case 1:
            {
                return ___connectionClient(this, in, __current);
            }
            case 2:
            {
                return ___findByName(this, in, __current);
            }
            case 3:
            {
                return ___getAllAvailableSong(this, in, __current);
            }
            case 4:
            {
                return ___ice_id(this, in, __current);
            }
            case 5:
            {
                return ___ice_ids(this, in, __current);
            }
            case 6:
            {
                return ___ice_isA(this, in, __current);
            }
            case 7:
            {
                return ___ice_ping(this, in, __current);
            }
            case 8:
            {
                return ___inscriptionClient(this, in, __current);
            }
            case 9:
            {
                return ___streamByName(this, in, __current);
            }
        }

        assert(false);
        throw new Ice.OperationNotExistException(__current.id, __current.facet, __current.operation);
    }

    protected void __writeImpl(IceInternal.BasicStream __os)
    {
        __os.startWriteSlice(ice_staticId(), -1, true);
        __os.endWriteSlice();
    }

    protected void __readImpl(IceInternal.BasicStream __is)
    {
        __is.startReadSlice();
        __is.endReadSlice();
    }

    public static final long serialVersionUID = 0L;
}