import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { 
  MatButtonModule,
  MatMenuModule,
  MatToolbarModule,
  MatIconModule,
  MatCardModule
 } from '@angular/material';

import { AppComponent } from './app.component';
import { MenuComponent } from './components/menu/menu.component';
import { SensorBasicDisplayComponent } from './components/sensor/sensor.display.basic.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    SensorBasicDisplayComponent,
  ],
  imports: [
    BrowserModule,
    MatButtonModule,
    MatMenuModule,
    MatToolbarModule,
    MatIconModule,
    MatCardModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
