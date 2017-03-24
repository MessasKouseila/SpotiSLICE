#!/usr/bin/bash
ipAdd=$1
port_iceStorm=$2
nameApp="CentralIceStorm"
ip_edna=`ip route get 1 | awk '{print $NF;exit}'`
rep_racine=`pwd`
rep_song="$rep_racine/Music"


echo "TopicManager.Proxy=$nameApp/TopicManager:default -h $ipAdd -p $port_iceStorm
Ice.Admin.InstanceName=publisher
IceMX.Metrics.Debug.GroupBy=id
IceMX.Metrics.ByParent.GroupBy=parent" > config.pub


echo "[server]
port = 8080
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