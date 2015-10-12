#!/usr/bin/env python

from pprint import pprint as pp

node_desc = {
    "architecture": {
      "platform_type": "x86_64",
      "smp_size": 2,
      "smt_size": 48
    },
    "bios": {
        "release_date": "03/09/2015",
        "vendor": "Dell Inc.",
        "version": 1.2  },
    "chassis": {
        "manufacturer": "Dell Inc.",
        "name": "PowerEdge R630",
        "serial": "4Q28C42"  },
    "type": "node"
}

def flatten_dict(obj, parent=""):
    if type(obj) is dict:
        new_dict = {}
        for key, value in obj.items():
            new_parent = ".".join(filter(bool, [parent, key]))
            new_value = flatten_dict(value, parent=new_parent)
            new_dict.update(new_value if type(new_value) is dict else ((new_parent, new_value),))
        return new_dict
    else:
        return obj

pp(node_desc)
print("")
pp(flatten_dict(node_desc))