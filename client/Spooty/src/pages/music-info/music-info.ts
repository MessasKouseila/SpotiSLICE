import {Component} from '@angular/core';
import {NavController, NavParams} from 'ionic-angular';
 
@Component({
	selector: 'page-movie-info',
    templateUrl: 'music-info.html'
})
 
export class MusicInfo {
     
    music: {};  
     
    constructor(private navController: NavController, private navParams: NavParams) {
        this.music = navParams.get('music');
    }   
}