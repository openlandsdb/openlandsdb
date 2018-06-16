#github.com/stepps00
#2018-05-19

import json
import geojson
import pprint
import time
import os
import optparse

#starting id of project
starting_id = 123456780
if __name__ == '__main__':

    opt_parser = optparse.OptionParser()

    #all runs of script require three options
    opt_parser.add_option('-s', '--source', dest='source', action='store', default=None, help='Name of source prefix')
    opt_parser.add_option('-i', '--input', dest='input', action='store', default=None, help='Input geojson file')
    opt_parser.add_option('-r', '--data_root', dest='data_root', action='store', default=None, help='/path/to/data/')

    options, args = opt_parser.parse_args()

    #yell stuff
    if not options.source:
        raise exception('No source given. Quitting.')

    if not options.input:
        raise exception('No input file given. Quitting.')

    if not options.data_root:
        raise exception('No data root given. Quitting.')

    with open(str(options.input), 'r') as input:

        data = geojson.load(input)
        features = data['features']

        for feature in features:

            #id updated by 2 for every record
            starting_id += 2
            id = starting_id

            props = feature['properties']
            geom = feature['geometry']

            #create blank json for new record
            import_record = {"id":id, "type":"feature"}

            #build all properties 
            import_props = {}
            for prop in props:
                import_props[str(options.source) + ':' + str(prop)] = props[prop]

            #non source props
            import_props['oldb:name'] = props['Loc_Nm']
            import_props['oldb:source_geometry'] = "padus"
            import_props['oldb:source_geometry_other'] = {}
            import_props['oldb:iso_country'] = "US"
            import_props['oldb:last_updated'] = int(time.time())
            import_props['oldb:notes'] = ""

            #mapshapered input file for lat/lon
            #import_props['oldb:centroid_lat'] = props['latitude']
            #import_props['oldb:centroid_lon'] = props['longitude']

            #del these, as they are not padus sourced
            #del import_props['oldb:longitude']
            #del import_props['oldb:latitude']

            #rebuild
            import_record['geometry'] = geom
            import_record['properties'] = import_props

            #create directory for file
            filename = str(options.data_root) + str(id)[:3] + '/' + str(id)[3:6] + '/' + str(id)[6:9] + '/' + str(id) + '.geojson'
            os.makedirs(os.path.dirname(filename))

            #now export the feature and save to a 111/111/111 directory format
            with open(str(options.data_root) + str(id)[:3] + '/' + str(id)[3:6] + '/' + str(id)[6:9] + '/' + str(id) + '.geojson', 'w') as output:

                #standardize output with sorted keys and indented json
                geojson.dump(import_record, output, indent=4)
                print 'created record: ' + str(id)