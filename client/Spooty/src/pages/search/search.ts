import { Component, NgZone } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import {WebService} from '../services/WebService';
import {MusicInfo} from '../music-info/music-info';
import { Platform, ToastController } from 'ionic-angular';
import { ConfigPage } from '../config/config';


//declare var SpeechRecognition: any;
declare var platform: any;
declare var window: any;

@Component({
  selector: 'page-search',
  templateUrl: 'search.html',
  providers: [WebService, ConfigPage]
})
/**
 * 
 */
export class SearchPage {
    musics: Array<any>;
    ip: string = '';
    recognition: any;
    ready: boolean = false;
    isWaiting: boolean = false;
    errorCordova : string = "No error";
    public textResult: string = "saisir une recher ici";
    public statusSpeaker : string;
    public resultText : string;
    public isRecognizing : boolean = true;
    public spokenWords : Array<string> = new Array<string>()
    counter : number = 0;


    constructor(private config: ConfigPage, private navParams: NavParams, public navCtrl: NavController, platform: Platform,public _zone: NgZone, public toastCtrl: ToastController, private webService: WebService) {
        platform = platform;
        this.ip = config.getIP();
        console.log("voila l'ip " + this.ip);
        platform.ready().then(() => { 
            this.ready = true;
            console.log("Recognition is " + this.recognition)
            if(window.SpeechRecognition)
            {
                this.recognition = new window.SpeechRecognition(); 
                this.recognition.start();

                this.recognition.continuous = true;
                this.recognition.lang = 'fr-FR';
                this.recognition.maxAlternatives = 3;
                this.recognition.onnomatch = (event => {
                    console.log('No match found.');
                });
                this.recognition.onstart = (event => {
                    console.log('Started recognition.');
                    this._zone.run(() => {
                        this.isRecognizing = true;
                        this.isWaiting = false;
                    })
                });

                this.recognition.onend = (event => {
                    console.log('Stopped recognition.');
                    this._zone.run(() => {
                        this.isRecognizing = false;
                        this.presentToast("Stopped recognition.")
                        this.isWaiting = false;
                    })
                });

                this.recognition.onerror = (event => {
                    console.log('Error...' + event.error);
                    this._zone.run(() => {		
                        this.errorCordova = 'Error'
                        this.isRecognizing = false;
                        this.presentToast("Error..." + event.error)
                        this.isWaiting = false;
                    }
                    )
                });

                this.recognition.onresult = (event => {
                        if (event.results) {
                            this._zone.run(() => {
                                var result = event.results[0];
                                this.spokenWords.push(result[0].transcript);
                                this.textResult = result[0].transcript;
                                console.log('Text: ' + result[0].transcript);
                                this.presentToast(this.resultText);
                                this.webService.searchMusics(this.textResult, '192.168.0.21').subscribe(
                                    data => {
                                        this.musics = data;
                                        console.log(this.musics);
                                    },
                                    err => {
                                        console.log(err);
                                    },
                                    () => console.log('Musics Search Complete')
                                )
                        }
                    )
                    this.isWaiting = false;
                            this.isRecognizing = false;
                    }
                });

            }
        });
    }
    /**
   * 
   * @param navCtrl 
   * @param speech 
   * @param webService 
   */
  

  /**
   * 
   * @param event 
   */
    searchMusicDB(event, key) {
        if(event.key == "Enter") {
            this.webService.searchMusics(event.target.value, this.ip).subscribe(
                data => {
                    this.musics = data;
                    console.log(this.musics);
                },
                err => {
                    console.log(err);
                },
                () => console.log('Musics Search Complete')
            );
        }
    }
    /**
     * 
     */
    sendMusics() {
        if (this.musics != null) {
            console.log(this.musics.values);
        }
        return this.musics;
    }
    /**
     * 
     * @param event 
     * @param music 
     */
    itemTapped(event, music) { 
        this.navCtrl.push(MusicInfo, {
            music: music
        });
    }
    presentToast(message) {
        let toast = this.toastCtrl.create({
            message: message,
            position : "middle",
            duration: 3000
        });
        toast.present();
    }


    SpeechToText() {
        this.statusSpeaker = 'Waiting...';
        if(!this.isRecognizing)
        {
            this.recognition.start();
            this.isRecognizing = true;
            this.isWaiting = true;
        }
        else
        {
            this.isWaiting = true;
        }
    }
}
