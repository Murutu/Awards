import { Component } from '@angular/core';

@Component({
  selector: 'github',
  templateUrl: './github.component.html',
  styleUrls: ['./github.component.css']
})
export class GithubComponent {
  constructor(){
      console.log('Github Component Init...');
  }
}
