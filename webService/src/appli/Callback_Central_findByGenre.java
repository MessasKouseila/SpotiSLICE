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

public abstract class Callback_Central_findByGenre
    extends IceInternal.TwowayCallback implements Ice.TwowayCallbackArg1<appli.music[]>
{
    public final void __completed(Ice.AsyncResult __result)
    {
        CentralPrxHelper.__findByGenre_completed(this, __result);
    }
}
