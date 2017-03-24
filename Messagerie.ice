module Central {

    interface Messagerie {
        void inscription(string addIp, string port, string addMac);
        void deconnexion(string addIp);
        void notify(string info);
    };

};
