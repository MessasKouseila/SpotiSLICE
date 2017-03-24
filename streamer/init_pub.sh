#!/usr/bin/bash
port_iceStorm=$1
port_edna="8080"
nameApp="CentralIceStorm"
ip_edna=`ip route get 1 | awk '{print $NF;exit}'`
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