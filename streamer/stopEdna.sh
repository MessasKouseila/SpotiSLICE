#!/usr/bin/bash
id=`ps -aux |egrep "python" |egrep "edna.py" | awk '{print $2}'`
kill -9 $id