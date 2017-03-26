module Central {

    interface Messagerie {
        void inscription(string addIp, string port);
        void deconnexion(string addIp);
        void notify(string info, string addIp);
    };

};
