import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainContentOverviewComponent } from './main-content-overview.component';

describe('MainContentOverviewComponent', () => {
  let component: MainContentOverviewComponent;
  let fixture: ComponentFixture<MainContentOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainContentOverviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainContentOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
