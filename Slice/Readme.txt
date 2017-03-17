Nom : MESSAS
prenom : KOUSEILA
groupe : ILSEN CLASSIQUE

--> le fichier interface.ice correspond à l'interface ice.
 qui va permettre la communication du client avec le serveur qui seront implémenté dans 2 langages différent.

--> Explication concernant l'interface ice :
 module Music{
 # une sequence de byte pour pouvoir lire et écrire la musique dans un fichier sous format mp3
 sequence<byte> song;
 # une sequence de chaîne de carractères permettant de stocker le nom de tous les musique disponible sur un serveur
 sequence<string> liste;
 	interface mp3{
  # permet de renvoyer une musique correspondant au nom de la musique donner en paramètre
 	 song findByName(string nameSong);
   # permet de renvoyer une musique correspondant a l'id de la musique donner en paramètre
 	 song findById(int idSong);
   # permet à un client de rajouter une musique dans le serveur,
   # en indiquant le nom de la musique, sont id, et le fichier en byte de la musique.
 	 void add(song theSong, string nameSong, int idSong);
   # permet de supprimer une musique depuis un serveur en indiquant sont nom
 	 void delete(string nameSong);
   # permet de renvoyer la liste de toutes les musiques disponible sur le serveur
 	 liste getALL();
 	};

 	interface controle{
 	    song filter(song theSong);
 	    song bass(song theSong, int level);
 	};
 };

--> dossier rendu nomé Slice:
* serveur_python contient les sources du serveur python.
- album : contient les musique qu'offre le serveurs.
- Serveur_python.py : code source du serveur que j'ai codé.
- Interface_ice.py : code generer par ice.

* Client_java contient les sources du client java
- Musique : contient le code source generer par ice
- Client : contient le code client que j'ai codé en java

* jlayer-1.0.1-1.jar : API java permettant de jouer un fichier mp3.

 --> explication sur le fonctionnement :
 le serveur écrit en python se lance via la commande suivante :
 python Serveur_python.py
 une fois lancer il parcours le répértoire album est crée un dictionnaire contenant le nom des musiques qu'il trouve
et associe à chaque nom de musique son chemin.
une fois le client lancer via la commande :
bash lunch.sh
qui va lancer la commande :
java -jar repertoirDuFichierJar/mp3_Kouceila.jar

une liste de chanson disponible sur le serveur local 127.0.0.1 serra afficher
si le client selectionne une chanson, elle serra télécharger depuis le serveur le un repertoir local du client
puis le client pourra la jouer
le client peut aussi ajouter une musique en allant dans le menu file => add music
il doit selectionner un fichier sous format mp3 et ainsi il serra automatiquement envoyer au serveur.


le serveur doit être lancer en 1er, puis des client java peuvent être lancer
2 musiques sont contenus dans le serveur dans ce rendu.
