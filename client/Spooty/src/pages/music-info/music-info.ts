import {Component} from '@angular/core';
import {NavController, NavParams} from 'ionic-angular';
import { AudioProvider } from 'ionic-audio';
@Component({
	selector: 'page-movie-info',
    templateUrl: 'music-info.html'
})
 
export class MusicInfo {
    myTracks: any[];
    allTracks: any[];
    music: any;
    selectedTrack: number;
    constructor(private navController: NavController, private navParams: NavParams, private _audioProvider: AudioProvider) {
        this.music = navParams.get('music');
            this.myTracks = [{
                src: 'http://'+ this.music.url,
                artist: this.music.author,
                title: this.music.title,
                art: 'assets/icon/player.png',
                preload: null // tell the plugin to preload metadata such as duration for this track, set to 'none' to turn off
            }];
    }
    ngAfterContentInit() {     
        // get all tracks managed by AudioProvider so we can control playback via the API
        this.allTracks = this._audioProvider.tracks; 
    }

    playSelectedTrack() {
        // use AudioProvider to control selected track 
        this._audioProvider.play(this.selectedTrack);
    }

    pauseSelectedTrack() {
        // use AudioProvider to control selected track 
        this._audioProvider.pause(this.selectedTrack);
    }
            
    onTrackFinished(track: any) {
        console.log('Track finished', track)
    }
}