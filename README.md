# Test mvt encoding

This repo is meant to contain test cases to verify our expectations about how mvt tiles should get encoded.

## Installation

There is a make file with targets for each installation step.

### Make a new virtualenv

    make virtualenv

This will create a new virtualenv in the current directory called "env", and will activate it.

### Python dependencies

    make pythondependencies

Installs the Mapzen `mapbox-vector-tile` repo from the github master branch. Will also install its dependencies, one of which is shapely, which will depend on libgeos-dev being available.

### Node dependencies

    make nodejsdependencies

Pulls in `pbf` and `vector-tile` node packages via npm.

### Encode using mapbox-vector-tile python library

    make encode

This will use the `mapbox-vector-tile` python library to encode an example tile written to `tile.mvt`.

### Decode using mapbox vector-tile nodejs library

    make decode

This will decode the example tile from `tile.mvt`, and print out the geometries. It prints out the raw geometry, and the geometry again with the y axis flipped.
