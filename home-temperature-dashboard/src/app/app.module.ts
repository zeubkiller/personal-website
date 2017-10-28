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
import { SensorComponent } from './components/sensor/sensor.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    SensorComponent
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
