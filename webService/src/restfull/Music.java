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

    @XmlElement(name="name")
    String name;
    @XmlElement(name="author")
    String author;
    @XmlElement(name="album")
    String album;
    @XmlElement(name="genre")
    String genre;
    @XmlElement(name="url")
    String url;

    public Music() {

    }
    public Music(appli.music music){
        this.name = music.name;
        this.author= music.author;
        this.album = music.album;
        this.genre = music.genre;
        this.url = music.url;
    }

    public Music(String name, String author, String album, String genre, String url) {
        this.name = name;
        this.author = author;
        this.album = album;
        this.genre = genre;
        this.url = url;
    }

    @Override
    public String toString(){
        try {
            // takes advantage of toString() implementation to format {"a":"b"}
            return new JSONObject().put("name", name).put("author", author).put("album", album).put("album", album).put("genre", genre).put("url", url).toString();
        } catch (JSONException e) {
            return null;
        }
    }
}