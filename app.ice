module appli {

    sequence<byte> song;
    struct music {
        string name;
        string author;
        string album;
        string genre;
        string url;
    };
    sequence<music> repository;

    /*
        interface de communication entre un streamer et le serveur Central
    */
	interface Streamer {
        // ajoute une music dans un server de stream
        void addSong(song theSong, string nameSong, string author, string album, string genre);
    };

    /*
        interface de communication entre un client et le serveur Central
    */
    interface Central {

        // renvoie la liste des musiques correspendant au nom donnée en paramètre
        repository findByName(string nameSong);
        repository findByAuth(string nameAuthor);
        repository findByAlbum(string nameAlbum);
        repository findByGenre(string nameGenre);

        // on recupere une ip et un port pour ajouter une musique sous format ip:port
        string getStreamer();
        
        // renvoie toutes les musiques disponibles
        repository getAllAvailableSong();
    };
};