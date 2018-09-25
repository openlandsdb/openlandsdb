#github.com/stepps00
#2018-06-16

import json
import geojson
import pprint
import time
import os
import optparse
import collections
import shapely.geometry

#starting id of project
starting_id = 123461354

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
            shape = shapely.geometry.asShape(geom)
            xy = shape.centroid

            #create blank json for new record
            import_record = {"id":id, "type":"Feature"}
            
            #build all properties 
            import_props = {}

            #all required  props
            import_props['geom:bounds'] = ",".join(map(str, list(shape.bounds)))
            import_props['geom:latitude'] = xy.y
            import_props['geom:longitude'] = xy.x
            import_props['geom:source'] = str(options.source)
            import_props['geom:source_alts'] = []
            import_props['label:latitude'] = props['latitude']
            import_props['label:longitude'] = props['longitude']
            import_props['ol:concordances'] = {"eea:site_code":str(props['SITE_CODE'])}
            import_props['ol:country'] = "AL"
            import_props['ol:date_modified'] = int(time.time())
            import_props['ol:land_designation'] = props['DESIGNATE'].split(' (')[0]
            import_props['ol:name'] = props['SITE_NAME']
            import_props['ol:note'] = ""
            import_props['ol:managing_agency'] = "Ministry of Environment of Albania"
            import_props['ol:managing_agency_level'] = "Federal"

            #rebuild
            import_record['properties'] = import_props
            import_record['geometry'] = shape

            #create directory for file
            filename = str(options.data_root) + str(id)[:3] + '/' + str(id)[3:6] + '/' + str(id)[6:9] + '/' + str(id) + '.geojson'
            os.makedirs(os.path.dirname(filename))

            #now export the feature and save to a 111/111/111 directory format
            with open(str(options.data_root) + str(id)[:3] + '/' + str(id)[3:6] + '/' + str(id)[6:9] + '/' + str(id) + '.geojson', 'w') as output:

                #standardize output with sorted keys and indented json
                geojson.dump(import_record, output, sort_keys = True, indent=4)
                print 'created record: ' + str(id)