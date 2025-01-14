#!/usr/bin/env python
class FilterModule(object):
  def filters(self):
    return { 'mapattributes': self.mapattributes }

  def mapattributes(self, list_of_dicts, list_of_keys):
    l = []
    for di in list_of_dicts:
      newdi = { }
      for key in list_of_keys:
        # newdi[key] = di[key]
        if di.get(key, None) != None:
          newdi[key] = di[key]

      l.append(newdi)
    return l