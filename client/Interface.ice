module Music{

sequence<byte> song;
sequence<string> liste;

	interface mp3{
	 song findByName(string nameSong);
	 song findById(int idSong);
	 void add(song theSong, string nameSong, int idSong);
	 void delete(string nameSong);
	 liste getALL();
	};

	interface controle{
	    song filter(song theSong);
	    song bass(song theSong, int level);    
	};
};
