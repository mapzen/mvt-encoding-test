var VectorTile = require('vector-tile').VectorTile;
var Protobuf = require('pbf');
var fs = require('fs');

if (process.argv.length < 3) {
    console.error('Usage: ' + process.argv[0] + ' ' + process.argv[1] + ' file-to-read.mvt');
    process.exit(1);
}

var filename = process.argv[2];
var data = fs.readFileSync(filename)

var tile = new VectorTile(new Protobuf(data));

var layer = tile.layers.layername;

for (var i = 0; i < 2; i++) {
  var feature = layer.feature(i);
  var geometryRaw = feature.loadGeometry();

  // flip the y axis
  var geometry = geometryRaw.map(function(coords) {
      return coords.map(function(coord) {
        return {x: coord.x, y: 4096 - coord.y };
    });
  });

  console.log('********************************************************************************');
  console.log('Feature ' + (i + 1));
  console.log('********************************************************************************');
  console.log('Raw geometry:');
  console.log(geometryRaw);
  console.log('Y axis flipped:');
  console.log(geometry);
}
