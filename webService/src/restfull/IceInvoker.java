package restfull;

import appli.CentralPrx;
import appli.StreamerPrx;


public class IceInvoker {
    int status = 0;
    com.zeroc.Ice.Communicator ic;
    com.zeroc.Ice.ObjectPrx base = null;
    CentralPrx loader = null;
    public IceInvoker(String ip) {
        ic = null;
        try {
            // changement de la taille max d'un message transmis
            com.zeroc.Ice.Properties datasize = com.zeroc.Ice.Util.createProperties();
            datasize.setProperty("com.zeroc.Ice.MessageSizeMax", "100024");
            com.zeroc.Ice.InitializationData initData = new com.zeroc.Ice.InitializationData();
            initData.properties = datasize;
            ic = com.zeroc.Ice.Util.initialize(initData);
            // definition du port et de l'ip du serveur
            base = ic.stringToProxy("Central:tcp -h "+ip+" -p 5000");
            loader = CentralPrx.checkedCast(base);
            if (loader == null)
                throw new Error("Invalid proxy");

        } catch (com.zeroc.Ice.LocalException e) {
            e.printStackTrace();
            status = 1;
        } catch (Exception e) {
            System.err.println(e.getMessage());
            status = 1;
        }
    }
}
