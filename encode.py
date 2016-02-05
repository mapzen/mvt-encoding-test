import mapbox_vector_tile
import sys

if len(sys.argv) == 0:
    print 'Usage: %s file-to-write.mvt' % sys.argv[0]
    sys.exit(1)

file_name = sys.argv[1]

# single polygon
geometry_poly = 'POLYGON ((10 10, 0 10, 0 0, 10 0, 10 10))'
# multipolygon containing 2 polygons, first containing a single outer
# ring, and the second containing outer and inner rings
# this example is taken from wikipedia
# https://en.wikipedia.org/wiki/Well-known_text
geometry_multi = ('MULTIPOLYGON ('
                  '((40 40, 20 45, 45 30, 40 40)), '
                  '((20 35, 10 30, 10 10, 30 5, 45 20, 20 35), '
                  '(30 20, 20 15, 20 25, 30 20)))')

properties = dict(foo='bar')
feature1 = dict(geometry=geometry_poly, properties=properties)
feature2 = dict(geometry=geometry_multi, properties=properties)
encoded = mapbox_vector_tile.encode([
    dict(name='layername', features=[feature1, feature2])
])
with open(file_name, 'wb') as fp:
    fp.write(encoded)
