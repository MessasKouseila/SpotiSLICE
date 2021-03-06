#!/usr/bin/bash
#########################################
# Auteur : MESSAS KOUSEILA
# Application : SpotiSLICE
# role du script : initialisation du serveur IceBox, IceStorm
# configuration du Subscriber
#########################################

ipAdd=`ip route get 1 | awk '{print $NF;exit}'`
port_iceStorm="10000"
port_iceBox="9996"
port_publisher="10001"
nameApp="CentralIceStorm"
timeout="2000"
db_name="central/db"
name_interface="Messagerie"

echo "IceStormAdmin.TopicManager.Default=$nameApp/TopicManager:default -h $ipAdd -p $port_iceStorm" > config.admin

echo "Ice.Admin.Endpoints=tcp -h $ipAdd -p $port_iceBox
Ice.Admin.InstanceName=icebox
IceBox.Service.IceStorm=IceStormService,37:createIceStorm --Ice.Config=config.service" > config.icebox

echo "IceStorm.InstanceName=$nameApp
IceStorm.TopicManager.Endpoints=default -h $ipAdd -p $port_iceStorm
IceStorm.Publish.Endpoints=tcp -h $ipAdd -p $port_publisher:udp -h $ipAdd -p $port_publisher
IceStorm.Flush.Timeout=$timeout
IceStorm.LMDB.Path=$db_name
Ice.Admin.InstanceName=icestorm
IceMX.Metrics.Debug.GroupBy=id
IceMX.Metrics.ByParent.GroupBy=parent" > config.service


echo "$name_interface.Subscriber.Endpoints=tcp -h $ipAdd:udp -h $ipAdd
TopicManager.Proxy=$nameApp/TopicManager:default -h $ipAdd -p $port_iceStorm
Ice.Admin.InstanceName=subscriber
IceMX.Metrics.Debug.GroupBy=id
IceMX.Metrics.ByParent.GroupBy=parent" > config.sub

echo "serveur IceBox tourne sur ip = $ipAdd   port = $port_iceBox"
icebox --Ice.Config=config.icebox
