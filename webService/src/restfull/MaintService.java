package restfull; /**
 * Created by kouceila on 18/04/17.
 */

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import java.util.ArrayList;
import java.util.List;
/*
* string streamByName(string nameSong);
* liste findByName(string nameSong);
* liste getAllAvailableSong();
* string getStreamer();
* */

// The Java class will be hosted at the URI path "/helloworld"
@Path("/")
public class MaintService {

    private Ice_inveker iceInvok = new Ice_inveker("192.168.0.21");
    // The Java method will process HTTP GET requests

    @GET
    @Produces("application/json")
    @Path("/getAll")
    public String getList(){
        int cpt = 1;
        List Musics = new ArrayList<Music>();
        for (String tmp_music : iceInvok.loader.getAllAvailableSong()) {
            Musics.add(new Music(tmp_music, "music"+cpt));
            cpt++;
        }
        return Musics.toString();
    }
}