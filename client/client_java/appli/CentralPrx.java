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

public interface CentralPrx extends Ice.ObjectPrx
{
    public boolean inscriptionClient(String login, String passWord);

    public boolean inscriptionClient(String login, String passWord, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord, Ice.Callback __cb);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord, java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord, Callback_Central_inscriptionClient __cb);

    public Ice.AsyncResult begin_inscriptionClient(String login, String passWord, java.util.Map<String, String> __ctx, Callback_Central_inscriptionClient __cb);

    public Ice.AsyncResult begin_inscriptionClient(String login, 
                                                   String passWord, 
                                                   IceInternal.Functional_BoolCallback __responseCb, 
                                                   IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_inscriptionClient(String login, 
                                                   String passWord, 
                                                   IceInternal.Functional_BoolCallback __responseCb, 
                                                   IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                   IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_inscriptionClient(String login, 
                                                   String passWord, 
                                                   java.util.Map<String, String> __ctx, 
                                                   IceInternal.Functional_BoolCallback __responseCb, 
                                                   IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_inscriptionClient(String login, 
                                                   String passWord, 
                                                   java.util.Map<String, String> __ctx, 
                                                   IceInternal.Functional_BoolCallback __responseCb, 
                                                   IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                   IceInternal.Functional_BoolCallback __sentCb);

    public boolean end_inscriptionClient(Ice.AsyncResult __result);

    public boolean connectionClient(String login, String passWord);

    public boolean connectionClient(String login, String passWord, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord, Ice.Callback __cb);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord, java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord, Callback_Central_connectionClient __cb);

    public Ice.AsyncResult begin_connectionClient(String login, String passWord, java.util.Map<String, String> __ctx, Callback_Central_connectionClient __cb);

    public Ice.AsyncResult begin_connectionClient(String login, 
                                                  String passWord, 
                                                  IceInternal.Functional_BoolCallback __responseCb, 
                                                  IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_connectionClient(String login, 
                                                  String passWord, 
                                                  IceInternal.Functional_BoolCallback __responseCb, 
                                                  IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                  IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_connectionClient(String login, 
                                                  String passWord, 
                                                  java.util.Map<String, String> __ctx, 
                                                  IceInternal.Functional_BoolCallback __responseCb, 
                                                  IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_connectionClient(String login, 
                                                  String passWord, 
                                                  java.util.Map<String, String> __ctx, 
                                                  IceInternal.Functional_BoolCallback __responseCb, 
                                                  IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                  IceInternal.Functional_BoolCallback __sentCb);

    public boolean end_connectionClient(Ice.AsyncResult __result);

    public String[] findByName(String nameSong);

    public String[] findByName(String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_findByName(String nameSong);

    public Ice.AsyncResult begin_findByName(String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_findByName(String nameSong, Ice.Callback __cb);

    public Ice.AsyncResult begin_findByName(String nameSong, java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_findByName(String nameSong, Callback_Central_findByName __cb);

    public Ice.AsyncResult begin_findByName(String nameSong, java.util.Map<String, String> __ctx, Callback_Central_findByName __cb);

    public Ice.AsyncResult begin_findByName(String nameSong, 
                                            IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                            IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_findByName(String nameSong, 
                                            IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                            IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                            IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_findByName(String nameSong, 
                                            java.util.Map<String, String> __ctx, 
                                            IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                            IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_findByName(String nameSong, 
                                            java.util.Map<String, String> __ctx, 
                                            IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                            IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                            IceInternal.Functional_BoolCallback __sentCb);

    public String[] end_findByName(Ice.AsyncResult __result);

    public String streamByName(String nameSong);

    public String streamByName(String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_streamByName(String nameSong);

    public Ice.AsyncResult begin_streamByName(String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_streamByName(String nameSong, Ice.Callback __cb);

    public Ice.AsyncResult begin_streamByName(String nameSong, java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_streamByName(String nameSong, Callback_Central_streamByName __cb);

    public Ice.AsyncResult begin_streamByName(String nameSong, java.util.Map<String, String> __ctx, Callback_Central_streamByName __cb);

    public Ice.AsyncResult begin_streamByName(String nameSong, 
                                              IceInternal.Functional_GenericCallback1<String> __responseCb, 
                                              IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_streamByName(String nameSong, 
                                              IceInternal.Functional_GenericCallback1<String> __responseCb, 
                                              IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                              IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_streamByName(String nameSong, 
                                              java.util.Map<String, String> __ctx, 
                                              IceInternal.Functional_GenericCallback1<String> __responseCb, 
                                              IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_streamByName(String nameSong, 
                                              java.util.Map<String, String> __ctx, 
                                              IceInternal.Functional_GenericCallback1<String> __responseCb, 
                                              IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                              IceInternal.Functional_BoolCallback __sentCb);

    public String end_streamByName(Ice.AsyncResult __result);

    public boolean add(byte[] theSong, String nameSong);

    public boolean add(byte[] theSong, String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong, java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong, Ice.Callback __cb);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong, java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong, Callback_Central_add __cb);

    public Ice.AsyncResult begin_add(byte[] theSong, String nameSong, java.util.Map<String, String> __ctx, Callback_Central_add __cb);

    public Ice.AsyncResult begin_add(byte[] theSong, 
                                     String nameSong, 
                                     IceInternal.Functional_BoolCallback __responseCb, 
                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_add(byte[] theSong, 
                                     String nameSong, 
                                     IceInternal.Functional_BoolCallback __responseCb, 
                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                     IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_add(byte[] theSong, 
                                     String nameSong, 
                                     java.util.Map<String, String> __ctx, 
                                     IceInternal.Functional_BoolCallback __responseCb, 
                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_add(byte[] theSong, 
                                     String nameSong, 
                                     java.util.Map<String, String> __ctx, 
                                     IceInternal.Functional_BoolCallback __responseCb, 
                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                     IceInternal.Functional_BoolCallback __sentCb);

    public boolean end_add(Ice.AsyncResult __result);

    public String[] getAllAvailableSong();

    public String[] getAllAvailableSong(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getAllAvailableSong();

    public Ice.AsyncResult begin_getAllAvailableSong(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getAllAvailableSong(Ice.Callback __cb);

    public Ice.AsyncResult begin_getAllAvailableSong(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getAllAvailableSong(Callback_Central_getAllAvailableSong __cb);

    public Ice.AsyncResult begin_getAllAvailableSong(java.util.Map<String, String> __ctx, Callback_Central_getAllAvailableSong __cb);

    public Ice.AsyncResult begin_getAllAvailableSong(IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_getAllAvailableSong(IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                     IceInternal.Functional_BoolCallback __sentCb);

    public Ice.AsyncResult begin_getAllAvailableSong(java.util.Map<String, String> __ctx, 
                                                     IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb);

    public Ice.AsyncResult begin_getAllAvailableSong(java.util.Map<String, String> __ctx, 
                                                     IceInternal.Functional_GenericCallback1<String[]> __responseCb, 
                                                     IceInternal.Functional_GenericCallback1<Ice.Exception> __exceptionCb, 
                                                     IceInternal.Functional_BoolCallback __sentCb);

    public String[] end_getAllAvailableSong(Ice.AsyncResult __result);
}