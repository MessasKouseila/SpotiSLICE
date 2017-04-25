package restfull; /**
 * Created by kouceila on 18/04/17.
 */

import org.json.JSONException;
import org.json.JSONObject;

import javax.ejb.Singleton;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import java.util.*;
/*
* string streamByName(string nameSong);
* liste findByName(string nameSong);
* liste getAllAvailableSong();
* string getStreamer();
* */

// The Java class will be hosted at the URI path "/helloworld"
@Path("/")
@Singleton
public class MaintService {

    private Ice_inveker iceInvok;
    // The Java method will process HTTP GET requests
    private Map Commande = new HashMap();
    public MaintService() throws InterruptedException {

        Commande.put("tout", "getAllAvailableSong");
        Commande.put("tous", "getAllAvailableSong");
        Commande.put("toutes", "getAllAvailableSong");
        Commande.put("all", "getAllAvailableSong");
        Commande.put("alls", "getAllAvailableSong");

        Commande.put("nom", "findByName");
        Commande.put("name", "findByName");

        Commande.put("auteur", "findByAuth");
        Commande.put("auteure", "findByAuth");
        Commande.put("author", "findByAuth");
        Commande.put("authors", "findByAuth");

        Commande.put("album", "findByAlbum");
        Commande.put("albums", "findByAlbum");


        Commande.put("genre", "findByGenre");
        Commande.put("genr", "findByGenre");
        Commande.put("genre", "findByGenre");
        Commande.put("genres", "findByGenre");
        Commande.put("style", "findByGenre");
        Commande.put("styles", "findByGenre");
        Commande.put("type", "findByGenre");
        Commande.put("types", "findByGenre");
        Commande.put("tipe", "findByGenre");
    }

    @GET
    @Produces("text/plain")
    @Path("/Init/{Ip}")
    public String Init(@PathParam("Ip") String Ip){

            if (this.iceInvok != null && !this.iceInvok.ic.isShutdown()) {
                this.iceInvok = null;
                this.iceInvok.ic.destroy();
            }
            this.iceInvok = new Ice_inveker(Ip);
            return "Ok";
    }

    @GET
    @Produces("application/json")
    @Path("/Vocal/{parole}")
    public String Vocal(@PathParam("parole") String parole) throws JSONException {
        int tmp = 0;
        String chaine = parole;
        Iterator it = this.Commande.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            if ( chaine.contains((pair.getKey()).toString()) ) {
                switch (pair.getValue().toString()) {
                    case "getAllAvailableSong":
                        return this.getAllAvailableSong();
                    case "findByName":
                        tmp = parole.indexOf(pair.getKey().toString());
                        tmp = tmp + pair.getKey().toString().length();
                        if (chaine.substring(tmp + 1).charAt(0) == ' ') {
                            break;
                        } else {
                            return this.findByName(chaine.substring(tmp + 1));
                        }
                    case "findByAuth":
                        tmp = parole.indexOf(pair.getKey().toString());
                        tmp = tmp + pair.getKey().toString().length();
                        if (chaine.substring(tmp + 1).charAt(0) == ' ') {
                            break;
                        } else {
                            return this.findByAuth(chaine.substring(tmp + 1));
                        }
                    case "findByAlbum":
                        tmp = parole.indexOf(pair.getKey().toString());
                        tmp = tmp + pair.getKey().toString().length();
                        if (chaine.substring(tmp + 1).charAt(0) == ' ') {
                            break;
                        } else {
                            return this.findByAlbum(chaine.substring(tmp + 1));
                        }
                    case "findByGenre":
                        tmp = parole.indexOf(pair.getKey().toString());
                        tmp = tmp + pair.getKey().toString().length();
                        if (chaine.substring(tmp + 1).charAt(0) == ' ') {
                            break;
                        } else {
                            return this.findByGenre(chaine.substring(tmp + 1));
                        }

                    default:
                        return "JE NE COMPREND PAS CE QUE TU DIT";
                }
            }
        }
        return null;
    }

    @GET
    @Produces("application/json")
    @Path("/getAllAvailableSong")
    public String getAllAvailableSong(){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.getAllAvailableSong()) {
            Musics.add(new Music(tmp_music));
        }
        return Musics.toString();
    }

    @GET
    @Produces("application/json")
    @Path("/findByName/{nameSong}")
    public String findByName(@PathParam("nameSong") String nameSong){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByName(nameSong)) {
            Musics.add(new Music(tmp_music));
        }
        return Musics.toString();
    }

    @GET
    @Produces("application/json")
    @Path("/findByAuth/{nameAuthor}")
    public String findByAuth(@PathParam("nameAuthor") String nameAuthor){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByAuth(nameAuthor)) {
            Musics.add(new Music(tmp_music));
        }
        return Musics.toString();
    }

    @GET
    @Produces("application/json")
    @Path("/findByAlbum/{nameAlbum}")
    public String findByAlbum(@PathParam("nameAlbum") String nameAlbum){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByAlbum(nameAlbum)) {
            Musics.add(new Music(tmp_music));
        }
        return Musics.toString();
    }

    @GET
    @Produces("application/json")
    @Path("/findByGenre/{nameGenre}")
    public String findByGenre(@PathParam("nameGenre") String nameGenre){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByGenre(nameGenre)) {
            Musics.add(new Music(tmp_music));
        }
        return Musics.toString();
    }

}