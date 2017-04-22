package restfull; /**
 * Created by kouceila on 22/04/17.
 */

import appli.CentralPrx;
import appli.CentralPrxHelper;
import appli.StreamerPrx;
import appli.StreamerPrxHelper;


public class Ice_inveker {
    int status = 0;
    Ice.Communicator ic = null;
    Ice.ObjectPrx base = null;
    CentralPrx loader = null;
    public Ice_inveker(String ip) {
        try {
            // changement de la taille max d'un message transmis
            Ice.Properties datasize = Ice.Util.createProperties();
            datasize.setProperty("Ice.MessageSizeMax", "100024");
            Ice.InitializationData initData = new Ice.InitializationData();
            initData.properties = datasize;
            ic = Ice.Util.initialize(initData);
            // definition du port et de l'ip du serveur
            base = ic.stringToProxy("Central:tcp -h "+ip+" -p 5000");
            loader = CentralPrxHelper.checkedCast(base);
            if (loader == null)
                throw new Error("Invalid proxy");

        } catch (Ice.LocalException e) {
            e.printStackTrace();
            status = 1;
        } catch (Exception e) {
            System.err.println(e.getMessage());
            status = 1;
        }
    }
}
