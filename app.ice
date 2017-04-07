module appli {

    sequence<byte> song;
    struct music {
        string name;
        string url;
    };
    sequence<music> repository;
    sequence<string> liste;

	interface Streamer {
        // ajoute une music dans un server de stream
        void addSong(song theSong, string nameSong);
    };

    /*
        interface de communication entre un client et le serveur Central
    */
    interface Central {

        // inscription d'un client au Central
        bool inscription(string login, string passWord);
        // connexion d'un client au serveur Central
        bool connection(string login, string passWord);
        // renvoie la liste des musiques correspendant au nom donnée en paramètre
        liste findByName(string nameSong);
        // lance le streaming de la musique choisie par le client
        string streamByName(string nameSong);
        // on recupere une ip et un port pour ajouter une musique sous format ip:port
        string getStreamer();
        // renvoie toutes les musiques disponibles
        liste getAllAvailableSong();
    };
};