// **********************************************************************
//
// Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.5.1
//
// <auto-generated>
//
// Generated from file `Interface.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Music;

public interface _mp3OperationsNC
{
    byte[] findByName(String nameSong);

    byte[] findById(int idSong);

    void add(byte[] theSong, String nameSong, int idSong);

    void delete(String nameSong);

    String[] getALL();
}
