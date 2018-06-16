#!/usr/bin/env python

from __future__ import unicode_literals

import os
import sys
import logging
import datetime
import json
import io

if __name__ == '__main__':

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)

    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    sources = os.path.join(root, 'sources/index')
    data = os.path.join(root, 'sources/spec')

    latest = os.path.join(data, "sources-list-master.json")
    readme = os.path.join(sources, "README.md")

    fh = io.open(latest, "r")
    spec = json.load(fh)

    lookup = {}

    for id, details in spec.items():
        lookup[details['name']] = id

    names = lookup.keys()
    names.sort()

    now = datetime.datetime.now()
    ymd = now.strftime("%Y-%m-%d")

    docs = io.open(readme, "w")
    docs.write("# openlands sources\n\n")

    for n in names:

        id = lookup[n]
        details = spec[id]

        docs.write("## %s\n\n" % (details['name']))

        if details.get('description'):
            docs.write("_%s_ \n\n" % (details['description']))

        for k in ('id','name','prefix','access_date','license_type','license_text'):
            if details[k] == '':
                continue
            docs.write("* **%s**: %s\n" % (k, details[k]))

        for k in ('url_license','url_download','url_home','url_archive'):
            if details[k] == '':
                continue
            docs.write("* **%s**: [%s](%s)\n" % (k, details[k], details[k]))

        docs.write("\n")

    docs.close()