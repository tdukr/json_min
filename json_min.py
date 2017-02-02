# -*- coding: utf-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

import simplejson
import json
input = open('trial.geojson','r')
output = open('test.geojson','w')

#starts the .geojson file with the crs defining 
output.write('{"type":"FeatureCollection","features":[')

data = simplejson.loads(input.read())

count = 0

def write_JSON(a,b):
    output.write('"'+str(a)+'":')
    output.write('"'+str(b)+'",')

for feature in data['features']:
    output.write('\n{"type":"Feature","geometry":{') #writes geometry
    for key, value in feature['geometry'].iteritems():
        write_JSON (key, value)
    output.write('}')
    output.write(',"properties":{') #writes properties
    for key, value in feature['properties'].iteritems():
        if not value == '' and value is not None:
            write_JSON (key, value)
    output.write('}},')

#closes the .geojson
output.write('],"type":"FeatureCollection"}')    