# openlandsdb

An openly licensed, global geo-database of public lands.

Data is provided under the Linux Foundation's Community Data License Agreement (CDLA).

## FAQ

### What is openlandsdb?

A database of public land geodata from local, state, regional, and national agencies. Each public land is represented in a single GeoJSON file (a "record") with:

  - A standard set of properties.
  - Optional, additional properties.
  - A stable identifier.
  - One or more geometry.

### How can I view records?

For now, navigate to the `/data` directory, and click through the directory to view each record.

### How can I download sets of records?

This feature is in development. The goal will be two-fold:

 - An interactive map that will display all records within a given radius.
 - Distribution files (see the `/dist` directory) in csv, geojson, sqlite, and shapefile formats.
