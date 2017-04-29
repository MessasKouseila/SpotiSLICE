import { Component } from '@angular/core';
import { Platform } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { AudioProvider } from 'ionic-audio';

import { TabsPage } from '../pages/tabs/tabs';

@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  myTracks: any[];
  allTracks: any[];
   
  constructor(private _audioProvider: AudioProvider) { 
    // plugin won't preload data by default, unless preload property is defined within json object - defaults to 'none'
    this.myTracks = [{
      src: 'http://192.168.1.20:8080/Le%20chant%20des%20partisans%20%28Paroles%29.mp3',
      artist: 'patri',
      title: 'Le chant des partisants',
      art: null,
      preload: 'none' // tell the plugin to preload metadata such as duration for this track, set to 'none' to turn off
    }];
  }
  
  ngAfterContentInit() {     
    // get all tracks managed by AudioProvider so we can control playback via the API
    this.allTracks = this._audioProvider.tracks; 
  }
  
  playSelectedTrack() {
    // use AudioProvider to control selected track 
    this._audioProvider.play(this.myTracks[0]);
  }
  
  pauseSelectedTrack() {
     // use AudioProvider to control selected track 
     this._audioProvider.pause(this.myTracks[0]);
  }
         
  onTrackFinished(track: any) {
    console.log('Track finished', track)
  } 
}
