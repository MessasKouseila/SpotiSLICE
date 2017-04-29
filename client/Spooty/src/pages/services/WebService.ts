import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
  
export class WebService {  
    static get parameters() {
        return [Http];
    }
  
    constructor(private http:Http) {
         
    }
  
    searchMusics(phrase, ip) {
        console.log(phrase);
        var url = 'http://' + encodeURI(ip) + ':33103/ISpot/Vocal/' + encodeURI(phrase);
        console.log(url);
        var response = this.http.get(url).map(res => res.json());
        return response;
    }
}