module appli {

    sequence<byte> song;
    sequence<string> liste;

    /*
        interface de communication entre un serveur de stockage et le serveur Central
    */
	interface serverCentral {
        // inscription d'un server au Central
        void inscriptionServer(string addIp, string addMac, string port);
        // connexion d'un server au CentralServer
        void connectionServer(string ID, string passWord);
        // deconnexion
        void deconnectionServer();
        // renvoie la liste des musiques stocker sur le server vers le Central
        liste getRepertoire();
        // le server informe le Central d'un changement sur son repertoire
        string notify();
        // forcer le server à se mettre à jour
        void update();
        // demande au server si il peut stocke une music
        bool addSong(song theSong);

    };

    /*
        interface de communication entre un client et le serveur Central
    */
    interface CentralClient {

        // inscription d'un client au Central
        void inscriptionClient(string login, string passWord);
        // connexion d'un client au serveur Central
        void connectionClient(string login, string passWord, string addIp);
        // renvoie la liste des musiques correspendant au nom donnée en paramètre
        liste findByName(string nameSong);
        // renvoie la liste des musiques de l'auteur donnée en paramètre
        liste findByAuthor(string nameAuthor);
        // lance le streaming de la musique choisie par le client
        song streamById(int idSong);
        // lance le streaming de la musique choisie par le client
        song streamByName(string nameSong);
        bool add(song theSong, string nameSong, string nameAuthor);
        liste getAllAvailableSong();

    };
};