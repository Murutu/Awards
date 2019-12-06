import { TestBed } from '@angular/core/testing';

import { Github.Service.TsService } from './github.service.ts.service';

describe('Github.Service.TsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: Github.Service.TsService = TestBed.get(Github.Service.TsService);
    expect(service).toBeTruthy();
  });
});
