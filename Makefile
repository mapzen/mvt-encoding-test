virtualenv:
	virtualenv env
	source env/bin/activate

pythondependencies:
	pip install -U git+https://github.com/mapzen/mapbox-vector-tile.git

nodejsdependencies:
	npm install pbf
	npm install vector-tile

encode:
	python encode.py tile.mvt

decode:
	node decode.js tile.mvt
