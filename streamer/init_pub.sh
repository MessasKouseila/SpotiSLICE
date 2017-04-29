#!/usr/bin/bash
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : initialisation du server de streaming
#########################################

function validateIP()
 {
         local ip=$1
         local stat=1
         if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
                OIFS=$IFS
                IFS='.'
                ip=($ip)
                IFS=$OIFS
                [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 \
                && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
                stat=$?
        fi
        return $stat
}

#Jusqu'a ce que la reponse soit composée par un nombre, j'attends la saisie
#echo "Donnez l'ip du server Central' ?"
#read ip_iceStorm
#validateIP $ip_iceStorm
#until [[ ${$?} -ne 0 ]]; do
#echo "Donnez l'ip du server Central' ?"
#read ip_iceStorm
#validateIP $ip_iceStorm
#done

#Jusqu'a ce que la reponse soit composée par un nombre, j'attends la saisie#
#until [[ ${port_iceStorm} =~ ^[0-9]+$ ]]; do
#echo "Donnez le port du server Central' ?"
#read port_iceStorm
#done

#echo "le central est sur l'ip : $ip_iceStorm   port :  $port_iceStorm"

port_edna="8080"
nameApp="CentralIceStorm"
ip_edna=`ip route get 1 | awk '{print $NF;exit}'`
ip_iceStorm=`ip route get 1 | awk '{print $NF;exit}'`
port_iceStorm="10000"
rep_racine=`pwd`
rep_song="$rep_racine/album"


echo "TopicManager.Proxy=$nameApp/TopicManager:default -h $ip_edna -p $port_iceStorm
Ice.Admin.InstanceName=publisher
IceMX.Metrics.Debug.GroupBy=id
IceMX.Metrics.ByParent.GroupBy=parent" > config.pub


echo "[server]
port = $port_edna
robots=0
template-dir = templates
resource-dir = resources
template = default_complex.ezt
fileinfo=1
zip = 0
binding-hostname = $ip_edna
log = -
[acl]
[sources]
dir1 = $rep_song = MP3
[extra]
debug_level = 0
days_new = 30" > edna-0.6/edna.conf

python StreamerMain.py