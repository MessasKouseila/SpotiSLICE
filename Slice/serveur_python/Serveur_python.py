# coding: utf-8

# Auteur : MESSAS KOUSEILA, M1 ILSEN CLASSIQUE
import sys, traceback, Ice, os, glob
import Music
import Ice
album = []
# on recupere le repertoir courrant
current_directory = os.getcwd()
# on recupere le chemin absolu du fichier de configuration
file_album = current_directory + "/album/"
listmyalbum = file_album + "*.mp3"
for i in glob.glob(listmyalbum):
    j = i.split("/")
    album.append(j[len(j)- 1])
# path of song
path_song = ""

class mp3I(Music.mp3):

    def findByName(self, nameSong, current=None):
        print ("nom de la music rechercher : {0}".format(nameSong))
        #nous allons cherche le chemun absolu de la music
        #puis le renvoyé sous forme de byte au client
        path_song = file_album + nameSong
        fichier = open(path_song, "rb")
        data = fichier.read()
        return data

    def findById(self, idSong, current=None):
        print ("Id de la music rechercher : {0}".format(idSong))

    # permet à un client d'ajouter une music au repertoir du serveur
    def add(self, theSong, nameSong, idSong, current=None):
        print ("nom de la music à ajouter : {0}\n id de la music à ajouter {1}".format(nameSong, idSong))
        path_to_write = file_album + "/" + nameSong
        fichier = open(path_to_write, "wb")
        fichier.write(theSong)
        fichier.flush()
    # permet à un client de supprimer une music de son repertoire, pour le moment un message est afficher
    def delete(self, nameSong, current=None):
        print ("nom de la music à supprimer : {0}".format(nameSong))
    # permet à un client qui viens de se connecter, la liste de toutes les music que le serveur peut offrir
    def getALL(self, current=None):
        return album


status = 0
ic = None
try:
    props = Ice.createProperties(sys.argv)
    # je redefinie la taille maximal d'un message pour qu'une music soit telecharger depusi un client
    props.setProperty("Ice.MessageSizeMax", "100024")
    id = Ice.InitializationData()
    id.properties = props
    ic = Ice.initialize(id)
    # on definit l'adapteur qui permet  client de communiquer avec le serveur
    # on definit aussi l'address du serveur et le port de communication
    adapter = ic.createObjectAdapterWithEndpoints("SongLoaderAdapteur", "tcp -h  10.104.21.113 -p 10000")
    object = mp3I()
    adapter.add(object, ic.stringToIdentity("SongLoader"))
    adapter.activate()
    ic.waitForShutdown()
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
