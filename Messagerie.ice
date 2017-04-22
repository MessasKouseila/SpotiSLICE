module Central {

    struct music {
        string name;
        string author;
        string album;
        string genre;
        string url;
    };
    sequence<music> repository;

    interface Messagerie {

        void refresh(string addIp);
        void delFromRep(string addIp, repository rep);
        void addToRep(string addIp, repository rep);
        void deconnexion(string addIp);
        void notify(string info, string addIp);
        void sendAlbum(string addIp, repository rep);
        
    };
};
