from osgeo import ogr
data = ogr.Open('/Users/ankitjha/Desktop/super2/area111.shp')
stop = 256
count = 0
print('Data Name:', data.GetName())
# get a layer with GetLayer('layername'/layerindex)
for layer in data:
    print('Layer Name:', layer.GetName())
    print('Layer Feature Count:', len(layer))
# each layer has a schema telling us what fields and geometric fields the features contain
    print('Layer Schema')
    layer_defn = layer.GetLayerDefn()
    for i in range(layer_defn.GetFieldCount()):
        print(layer_defn.GetFieldDefn(i).GetName())
# some layers have multiple geometric feature types
# most of the time, it should only have one though
    for i in range(layer_defn.GetGeomFieldCount()):
# some times the name doesn't appear
# but the type codes are well defined
        print(layer_defn.GetGeomFieldDefn(i).GetName(), layer_defn.GetGeomFieldDefn(i).GetType())
# get a feature with GetFeature(featureindex)
# this is the one where featureindex may not start at 0
    layer.ResetReading()
    for feature in layer:
        count += 1
        print('Feature Geometry:', feature.geometry())
        if count == stop:
           wkt = str(feature.geometry())
           pt = ogr.CreateGeometryFromWkt(wkt)
           bufferDistance = 200
           poly = pt.Buffer(bufferDistance)
           print(poly.ExportToWkt())
    break
#print('Feature ID:', feature.GetFID())
# get a metadata field with GetField('fieldname'/fieldindex)
#print('Feature Metadata Keys:', feature.keys())
#print('Feature Metadata Dict:', feature.items())
#
#break