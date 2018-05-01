#!/usr/bin/bash
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : arret du server de streaming
#########################################
id=`ps -aux |egrep "python" |egrep "$1" | awk '{print $2}'`
kill -9 $id