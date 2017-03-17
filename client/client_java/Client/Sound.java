package Client;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.advanced.AdvancedPlayer;

public class Sound implements Runnable {
	public Sound(String path) throws Exception {
		InputStream in = (InputStream)new BufferedInputStream(new FileInputStream(new File(path)));
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
private boolean isPlaying = false;
private AdvancedPlayer player = null;
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
