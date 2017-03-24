module appli {

    sequence<byte> song;

    struct music {
        string name;
        string url;
    };
    sequence<music> repository;
    sequence<string> liste;

    /*
        interface de communication entre un serveur de stockage streamer et le serveur Central
    */
	interface Streamer {
        // renvoie la liste des musiques stocker sur le server vers le Central
        repository getRepertoire();
        // ajoute une music dans un server de stream
        bool addSong(song theSong, string nameSong);
        // on verifie que le server de stream peut toujours streamer une musique
        bool checkStream(string nameSong);
    };

    /*
        interface de communication entre un client et le serveur Central
    */
    interface Central {

        // inscription d'un client au Central
        bool inscriptionClient(string login, string passWord);
        // connexion d'un client au serveur Central
        bool connectionClient(string login, string passWord);
        // renvoie la liste des musiques correspendant au nom donnée en paramètre
        liste findByName(string nameSong);
        // lance le streaming de la musique choisie par le client
        string streamByName(string nameSong);
        bool add(song theSong, string nameSong);
        liste getAllAvailableSong();
    };
};