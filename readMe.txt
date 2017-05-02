ReadMe pour application architecture distribué
application : SpotySLICE
Nom et prénom : MESSAS KOUSEILA
Groupe : ILSEN CLASSIQUE

l'applciation comporte 4 volet important : 
- les serveurs de streaming
- le serveur central
- les webservice
- l'application mobile


############################
## fonctionnement general ## 
############################

- on lance via la commande ci-dessous le serveur icebox qui utilise la technologie ICE de zeroC afin d'avoir un dépôt de message 
afin d'utilisé la communication asynchrone par message ( similaire à JMS pour Java Message Service d'oracale).

bash central/init.sh 

- on lance le serveur central qui va être sur ecoute sur le depôt de message afin de traiter les messages 
qui y sont déposés par les serveurs de streaming

python central/CentralServerMain.py

- on lance un serveur de streaming qui lui va analysé le repertoir 'album' afin de recuperer les musiques qu'il peut streamer 
( mettre à disposition via un streaming), 
puis une fois le scan fini, il met à joursa bdd local, il envoie un message sur le dépôt de message avec toutes les musiques 
dont il dispose afin que le central mette à jour la bdd_Central

bash streamer/init_pub.sh

- on lance le webService (RestFul JEE webService) en deployant l'archive sur un serveur d'application de type glassfish 
ou tomcat ou autre

- on lance l'application mobile et on configure l'ip en mettant l'ip du web service sur la page de onfig, 
en se deplace vers la page search afin d'utiliser la commande vocalet écouter les musics disponible

####################################
### details sur l'implémentation ###
####################################

code source de l'application sur gitHub : https://github.com/MessasKouseila/SpotiSLICE

chaque script à un en-tête qui details son utilité
partie 1 : Serveur Central 
- repertoir : central
- implémentation : python, Ice, IceStorm ( subscriber, il recupere les messages envoyé par les Publisher puis les traite)
- role : gerer la bdd central, gerer la communication avec le webService

partie 2 : Serveur streaming
- repertoir : streamer
album : repertoir de musique
edna 0.6 : permet de streamer la musique disponible sur le repertoir album

- implémentation : python, Ice, IceStorm (Publisher, il envoie des messages sur le depôt de message)
- role : stocker de la musiques, streamer de la musiques

partie 3 : webService
- repertoir : webService
MaintService.java contient le code des webservice
Ice_inveker.java contient le code qui permet la communication avec le serveur Central

- implémentation : Java, JEE, glassfish (serveur d'applciation), JAX-rs, Json
- Rôle : interpréter les chaines de caractères envoyés par les clients mobiles, recupere les informations depuis le serveur central, 
renvoyé les données vers le client mobile sous format JSON

partie 4 : client mobile
- implémentation : Ionic 2 qui permet d'avoir une application compatible sur Android, IOS et WindowsPhone (si si y a des gens sur windowsPhone) , AngularJS 2, TypeScript
- Rôle : recupere la parole puis la transmet vers le SpeechRecognition afin d'avoir la chaine de caractères qui correspond
puis fait appele au webService afin d'interpréter la chaine de caractères, afiche enfin les resultats obtenu 
et permet de lire la musique. 
