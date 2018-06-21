# openlandsdb

An openly licensed, global geo-database of public lands.

## License

Data is provided by openlandsdb under [CC BY](https://creativecommons.org/licenses/by/1.0) license.

All data sources used by openlandsdb can be found [here](https://github.com/openlandsdb/openlandsdb/blob/master/sources/index/README.md).

Source data used by openlandsdb is provided under a CC BY, public domain, or equivalent license.

No use restrictions.

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

### Hasn't this been done before?

No - similar databases are available online, but most contain commercial (and other) use restrictions; openlandsdb is provided without use restrictions.

### How can I help?

We are always happy to collaborate about a data contribution or chat about an issue. Follow the instructions in the [contributing.md](https://github.com/openlandsdb/openlandsdb/blob/master/CONTRIBUTING.md) file to file an issue.
