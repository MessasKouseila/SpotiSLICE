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

public class music implements java.lang.Cloneable, java.io.Serializable
{
    public String name;

    public String url;

    public music()
    {
        name = "";
        url = "";
    }

    public music(String name, String url)
    {
        this.name = name;
        this.url = url;
    }

    public boolean
    equals(java.lang.Object rhs)
    {
        if(this == rhs)
        {
            return true;
        }
        music _r = null;
        if(rhs instanceof music)
        {
            _r = (music)rhs;
        }

        if(_r != null)
        {
            if(name != _r.name)
            {
                if(name == null || _r.name == null || !name.equals(_r.name))
                {
                    return false;
                }
            }
            if(url != _r.url)
            {
                if(url == null || _r.url == null || !url.equals(_r.url))
                {
                    return false;
                }
            }

            return true;
        }

        return false;
    }

    public int
    hashCode()
    {
        int __h = 5381;
        __h = IceInternal.HashUtil.hashAdd(__h, "::appli::music");
        __h = IceInternal.HashUtil.hashAdd(__h, name);
        __h = IceInternal.HashUtil.hashAdd(__h, url);
        return __h;
    }

    public music
    clone()
    {
        music c = null;
        try
        {
            c = (music)super.clone();
        }
        catch(CloneNotSupportedException ex)
        {
            assert false; // impossible
        }
        return c;
    }

    public void
    __write(IceInternal.BasicStream __os)
    {
        __os.writeString(name);
        __os.writeString(url);
    }

    public void
    __read(IceInternal.BasicStream __is)
    {
        name = __is.readString();
        url = __is.readString();
    }

    static public void
    __write(IceInternal.BasicStream __os, music __v)
    {
        if(__v == null)
        {
            __nullMarshalValue.__write(__os);
        }
        else
        {
            __v.__write(__os);
        }
    }

    static public music
    __read(IceInternal.BasicStream __is, music __v)
    {
        if(__v == null)
        {
             __v = new music();
        }
        __v.__read(__is);
        return __v;
    }
    
    private static final music __nullMarshalValue = new music();

    public static final long serialVersionUID = -1451822465511873406L;
}