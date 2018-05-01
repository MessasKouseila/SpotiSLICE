package Client;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JDesktopPane;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.filechooser.FileSystemView;


public class Client_graphics {
	
	Font trbi = new Font("TimesRoman", Font.BOLD+Font.ITALIC, 16);
	private JFrame frame;
	private JDesktopPane container;
	private JPanel panel_option;
	private JLabel current_song_label;
	private JLabel liste_song_label;
	private JLabel option_label;
	private JList<String> listOfSong;
	private JButton btnPlay;
	private JButton btnStop;
	private JButton btnUpdate;
	private JButton btnDelete;
	private Sound readerSong;
	private FileSystemView vueSysteme; 
	private DefaultListModel<String> model;
	//récupération des répertoires 
	private File defaut;
	private File home;
	//création et affichage des JFileChooser 
	private JFileChooser defautChooser;
	int width = 768;
	int height = 1024;
	// ************** *******///
	public Thread download;
	public Client_java client;
	public String[] listeOfsong = {};
	public FileOutputStream fileOuputStream;
	byte[] uneMusic;
	byte[] envoie;
	String tmp;
	StringBuilder nameMusic;
	public String path = "";
	public Thread playIt;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
					Client_graphics window = new Client_graphics();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});

	}
	
	public Client_graphics() {
		
		vueSysteme = FileSystemView.getFileSystemView();
		defaut = vueSysteme.getDefaultDirectory(); 
		home = vueSysteme.getHomeDirectory();
		// on crée un cleint qui va communqiuer avec le serveur python
		client = new Client_java("127.0.0.1");
		// appel de la methode getAll sur le serveur via l'adaptateur ICE
		listeOfsong = client.loader.getAllAvailableSong();
		model = new DefaultListModel<String>();
		for(String i : listeOfsong) {
			model.addElement(i);
		}
		// initialisation de l'interface graphique
		initialize();
		
	}
	
	private void initialize() {
		Dimension dimension = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
		height = (int)dimension.getHeight();
		width  = (int)dimension.getWidth();
		
		
		/// ********** fenetre principale *******************///
		frame = new JFrame();
		frame.setTitle("Client_mp3");
		frame.setAlwaysOnTop(false);
		frame.setResizable(false);
		frame.setBounds((width - 500) /  2, (height - 350) / 2, 500, 450);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		frame.getContentPane().setBackground(new Color(109, 132, 180));
		/// ********** conteneur principale *******************///
		container = new JDesktopPane();
		container.setSize(frame.getWidth(), frame.getHeight());
		frame.getContentPane().add(container);
		/// ********** liste des musics *******************///
		
		liste_song_label = new JLabel("     Liste des Chansons     ");
		liste_song_label.setFont(trbi);
		liste_song_label.setBackground(new Color(220, 226, 36));
		liste_song_label.setBounds(0, 0, 300, 26);
		liste_song_label.setOpaque(true);
		container.add(liste_song_label);
			
		listOfSong = new JList<String>(model);
		listOfSong.addListSelectionListener(new ListSelectionListener() {
			
			@SuppressWarnings("deprecation")
			@Override
			public void valueChanged(ListSelectionEvent e) {
				current_song_label.setText((String)listOfSong.getSelectedValue());
				try { 
					path = "http://";
					tmp = (String)listOfSong.getSelectedValue();
					if (tmp != null) {
						nameMusic = new StringBuilder();
						for (int i = 0; i < tmp.length(); ++i) {
							if (tmp.charAt(i) == ' ') {
								nameMusic.append("%20");
							} else {
								nameMusic.append(tmp.charAt(i));
							}
						}
		                path = path + nameMusic.toString();
		                System.out.println(path);
		                btnPlay.setEnabled(true);
						btnDelete.setEnabled(true);
					}
             	} catch (Exception e1){
            	 	e1.printStackTrace();
             	}

			}
		});
		listOfSong.setBounds(0, 27, 300, 327);
		container.add(listOfSong);
		
		
		/// ********** panel  ptionalitées *******************///
		option_label = new JLabel("       Options       ");
		option_label.setBounds(300, 0, 270, 26);
		option_label.setFont(trbi);
		option_label.setBackground(new Color(0, 204, 0));
		option_label.setOpaque(true);
		container.add(option_label);
		
		panel_option = new JPanel();
		panel_option.setBounds(300, 27, 200, 327);
		container.add(panel_option);
		panel_option.setLayout(null);
		
		current_song_label = new JLabel("aucune music selectionne");
		current_song_label.setBounds(8, 5, 183, 15);
		panel_option.add(current_song_label);
		
		btnPlay = new JButton(" PLAY ");
		btnPlay.setEnabled(false);
		btnPlay.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				try {
					readerSong = new Sound(path);
					btnPlay.setEnabled(true);
					playIt = new Thread(readerSong);
					playIt.start();
					btnStop.setEnabled(true);
				} catch (Exception e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
		});
		btnPlay.setBounds(20, 25, 76, 25);
		panel_option.add(btnPlay);
		
		btnStop = new JButton(" STOP ");
		btnStop.setEnabled(false);
		btnStop.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				try {
					if (!playIt.isInterrupted())
						playIt.stop();
				} catch (Exception e1) {
					//e1.printStackTrace();
				}
			}
		});
		btnStop.setBounds(101, 25, 79, 25);
		panel_option.add(btnStop);
		
		btnUpdate = new JButton("Update");
		btnUpdate.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				listeOfsong = client.loader.getAllAvailableSong();
				model.clear();
				for(String i : listeOfsong) {
					model.addElement(i);
				}
				listOfSong.setModel(model);
				
			}
		});
		btnUpdate.setBounds(42, 83, 117, 25);
		panel_option.add(btnUpdate);
		
		btnDelete = new JButton(" DELETE ");
		btnDelete.setEnabled(false);
		btnDelete.setBounds(54, 55, 92, 25);
		//panel_option.add(btnDelete);
		/// ******** Menu de l'application cote client ******************///////////////
		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);
		menuBar.setBackground(new Color(109, 132, 180));
		
		// menu file
		JMenu menu_File = new JMenu("File");
		menuBar.add(menu_File);
		JMenuItem File_add = new JMenuItem("Add music");
		File_add.addMouseListener(new MouseAdapter() {
			//@Override
			public void mousePressed(MouseEvent e) {
				System.out.println("Ajout d'un fichier au serveur");
				defautChooser = new JFileChooser(defaut);
				int result = defautChooser.showOpenDialog(null);
				String[] toSplit = null; 
				if (result == JFileChooser.APPROVE_OPTION) {
				    // user selects a file
					File selectedFile = defautChooser.getSelectedFile();
					System.out.println("Selected file: " + selectedFile.getAbsolutePath());
					try {
						envoie = Files.readAllBytes(new File(selectedFile.getAbsolutePath()).toPath());
						toSplit = selectedFile.getAbsolutePath().split("/");
						System.out.println("Envoie de la music "+ toSplit[toSplit.length - 1]);
						//client.loader.add(envoie, toSplit[toSplit.length - 1], 0);
						System.out.println("Envoie termienr !! ");
					} catch (IOException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
				}
			}
		});
		menu_File.add(File_add);
		
		JMenuItem File_Close = new JMenuItem("Close");
		File_Close.addMouseListener(new MouseAdapter() {
			//@Override
			public void mousePressed(MouseEvent e) {
				if (client.ic != null) {
					// Clean up
					try {
						client.ic.destroy();
					} catch (Exception e1) {
						System.err.println(e1.getMessage());
					}
				}
				System.exit(0);
			}
		});
		menu_File.add(File_Close);
		
		// menu about
		JMenu menu_about = new JMenu("about");
		menuBar.add(menu_about);
		// menu help
		JMenu menu_Help = new JMenu("Help");
		menuBar.add(menu_Help);
		
	}
}
