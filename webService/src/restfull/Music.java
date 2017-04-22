package restfull;

import org.json.JSONException;
import org.json.JSONObject;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

/**
 * Created by kouceila on 21/04/17.
 */
@XmlRootElement
public class Music {
    @XmlElement(name="URL")
    String url_song;

    @XmlElement(name="nameSong")
    String name_song;

    public Music(){
    }

    public Music(String urlSong, String nameSong) {
        this.url_song = urlSong;
        this.name_song = nameSong;
    }

    @Override
    public String toString(){
        try {
            // takes advantage of toString() implementation to format {"a":"b"}
            return new JSONObject().put("URL", url_song).put("nameSong", name_song).toString();
        } catch (JSONException e) {
            return null;
        }
    }
}