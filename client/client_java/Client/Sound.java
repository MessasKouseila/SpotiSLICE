package Client;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.advanced.AdvancedPlayer;

public class Sound implements Runnable {
	
	public static InputStream openStream(String uneUrl) throws IOException {
	    final URL url = new URL(uneUrl);
	    final URLConnection con = url.openConnection();
	    con.setRequestProperty("User-Agent", "My Client");
	    return con.getInputStream();
	}
	
	private boolean isPlaying = false;
	private AdvancedPlayer player = null;
	
	public Sound(String path) throws Exception {
		InputStream in = openStream(path);
		player = new AdvancedPlayer(in);
	}
	
	public void play() throws Exception {
		if (player != null) {
			try {
				isPlaying = true;
				player.play();
			} catch (JavaLayerException e) {
				e.printStackTrace();
			}
		}
	}


	public void stop() {
		if (isPlaying) {
			try {
				isPlaying = false;
				player.stop();
			} catch (Exception e1) {
				e1.printStackTrace();
			}
		}

	}

	public boolean isPlaying() {
		return isPlaying;
	}

	@Override
	public void run() {
		try {
			this.play();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
