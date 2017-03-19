import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';

import { MaterialModule } from '@angular/material';
import 'hammerjs';
import { MainMenuLeftComponent } from './main-menu-left/main-menu-left.component';
import { MainContentOverviewComponent } from './main-content-overview/main-content-overview.component';

@NgModule({
  declarations: [
    AppComponent,
    MainMenuLeftComponent,
    MainContentOverviewComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
