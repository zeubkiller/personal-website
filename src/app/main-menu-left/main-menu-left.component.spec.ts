import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainMenuLeftComponent } from './main-menu-left.component';

describe('MainMenuLeftComponent', () => {
  let component: MainMenuLeftComponent;
  let fixture: ComponentFixture<MainMenuLeftComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainMenuLeftComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainMenuLeftComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
