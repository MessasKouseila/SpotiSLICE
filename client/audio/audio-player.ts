import { Component } from '@angular/core';
import {Player} from '../../providers/player'
/*
  Generated class for the AudioPlayer component.

  See https://angular.io/docs/ts/latest/api/core/index/ComponentMetadata-class.html
  for more info on Angular 2 Components.
*/
@Component({
  selector: 'audio-player',
  templateUrl: 'audio-player.html'
  
})
export class AudioPlayerComponent {

  //text: string;
  //player = Player;
  constructor(public player:Player) {
    console.log('Hello AudioPlayer Component');
    //this.text = 'Hello World';
    
  }
  initTrack(audio)
  {
    this.player.initTrack(audio);
  }
  
}
