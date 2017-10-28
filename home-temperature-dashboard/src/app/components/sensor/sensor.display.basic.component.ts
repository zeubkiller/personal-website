import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'home-sensor-sensor-display-basic',
  templateUrl: './sensor.display.basic.component.html',
  styleUrls: ['./sensor.display.basic.component.css']
})
export class SensorBasicDisplayComponent implements OnInit {

  @Input() public value : string = "NaN";
  @Input() public unit : string = "";

  constructor() { }

  ngOnInit() {
  }

}
