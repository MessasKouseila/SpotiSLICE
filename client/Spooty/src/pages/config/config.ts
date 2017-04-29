import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-config',
  templateUrl: 'config.html'
})
export class ConfigPage {
    static textIP: string = "192.168.0.21";
    constructor(public navCtrl: NavController) {

    }
    changeIp(event) {
        if(event.key == "Enter") {
            ConfigPage.textIP = event.target.value;
            console.log(this.getIP());
        }
    }
    getIP() {
        return ConfigPage.textIP;
    }

}
