package restfull; /**
 * Created by kouceila on 18/04/17.
 */

import org.json.JSONException;

import javax.ejb.Singleton;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Response;
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
        Commande.put("Tout", "getAllAvailableSong");
        Commande.put("Tous", "getAllAvailableSong");
        Commande.put("Toutes", "getAllAvailableSong");
        Commande.put("All", "getAllAvailableSong");
        Commande.put("Alls", "getAllAvailableSong");


        Commande.put("nom", "findByName");
        Commande.put("name", "findByName");
        Commande.put("Nom", "findByName");
        Commande.put("Name", "findByName");

        Commande.put("auteur", "findByAuth");
        Commande.put("auteure", "findByAuth");
        Commande.put("author", "findByAuth");
        Commande.put("authors", "findByAuth");

         Commande.put("Auteur", "findByAuth");
        Commande.put("Auteure", "findByAuth");
        Commande.put("Author", "findByAuth");
        Commande.put("Authors", "findByAuth");

        Commande.put("album", "findByAlbum");
        Commande.put("albums", "findByAlbum");
        Commande.put("Album", "findByAlbum");
        Commande.put("Albums", "findByAlbum");


        Commande.put("genre", "findByGenre");
        Commande.put("genr", "findByGenre");
        Commande.put("genre", "findByGenre");
        Commande.put("genres", "findByGenre");
        Commande.put("style", "findByGenre");
        Commande.put("styles", "findByGenre");
        Commande.put("type", "findByGenre");
        Commande.put("types", "findByGenre");
        Commande.put("tipe", "findByGenre");
        
         Commande.put("Genre", "findByGenre");
        Commande.put("Genr", "findByGenre");
        Commande.put("Genre", "findByGenre");
        Commande.put("Genres", "findByGenre");
        Commande.put("Style", "findByGenre");
        Commande.put("Styles", "findByGenre");
        Commande.put("Type", "findByGenre");
        Commande.put("Types", "findByGenre");
        Commande.put("Tipe", "findByGenre");
    }

    @GET
    @Produces("text/plain")
    @Path("/Init/{Ip}")
    public Response Init(@PathParam("Ip") String Ip){

            if (this.iceInvok != null && !this.iceInvok.ic.isShutdown()) {
                this.iceInvok = null;
                this.iceInvok.ic.destroy();
            }
            this.iceInvok = new Ice_inveker(Ip);
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity("ok")
                .build();
    }

    @GET
    @Produces("application/json")
    @Path("/Vocal/{parole}")
    public Response Vocal(@PathParam("parole") String parole) throws JSONException {
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
                        return Response
                                .status(200)
                                .header("Access-Control-Allow-Origin", "*")
                                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                                .header("Access-Control-Allow-Credentials", "true")
                                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                                .header("Access-Control-Max-Age", "1209600")
                                .entity("JE NE COMPREND PAS CE QUE TU DIT")
                                .build();
                }
                }
            }
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity("WALOU !!!!!")
                .build();
        }

    @GET
    @Produces("application/json")
    @Path("/getAllAvailableSong")
    public Response getAllAvailableSong(){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.getAllAvailableSong()) {
            Musics.add(new Music(tmp_music));
        }

        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity(Musics.toString())
                .build();
    }

    @GET
    @Produces("application/json")
    @Path("/findByName/{nameSong}")
    public Response findByName(@PathParam("nameSong") String nameSong){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByName(nameSong)) {
            Musics.add(new Music(tmp_music));
        }
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity(Musics.toString())
                .build();
    }

    @GET
    @Produces("application/json")
    @Path("/findByAuth/{nameAuthor}")
    public Response findByAuth(@PathParam("nameAuthor") String nameAuthor){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByAuth(nameAuthor)) {
            Musics.add(new Music(tmp_music));
        }
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity(Musics.toString())
                .build();
    }

    @GET
    @Produces("application/json")
    @Path("/findByAlbum/{nameAlbum}")
    public Response findByAlbum(@PathParam("nameAlbum") String nameAlbum){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByAlbum(nameAlbum)) {
            Musics.add(new Music(tmp_music));
        }
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity(Musics.toString())
                .build();
    }

    @GET
    @Produces("application/json")
    @Path("/findByGenre/{nameGenre}")
    public Response findByGenre(@PathParam("nameGenre") String nameGenre){
        List Musics = new ArrayList<Music>();
        for (appli.music tmp_music : iceInvok.loader.findByGenre(nameGenre)) {
            Musics.add(new Music(tmp_music));
        }
        return Response
                .status(200)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Headers", "origin, content-type, accept, authorization")
                .header("Access-Control-Allow-Credentials", "true")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, HEAD")
                .header("Access-Control-Max-Age", "1209600")
                .entity(Musics.toString())
                .build();
    }

}