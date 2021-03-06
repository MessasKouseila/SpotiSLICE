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

public final class StreamerHolder extends Ice.ObjectHolderBase<Streamer>
{
    public
    StreamerHolder()
    {
    }

    public
    StreamerHolder(Streamer value)
    {
        this.value = value;
    }

    public void
    patch(Ice.Object v)
    {
        if(v == null || v instanceof Streamer)
        {
            value = (Streamer)v;
        }
        else
        {
            IceInternal.Ex.throwUOE(type(), v);
        }
    }

    public String
    type()
    {
        return _StreamerDisp.ice_staticId();
    }
}
