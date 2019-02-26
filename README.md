# parser-photoemission

## Setup and run example

We are currently targeting Python 3.6

Best use a virtual environment:
```
virtualenv -p python3 .pyenv
source .pyenv/bin/activate
```

Clone and install the nomad infrastructure and the necessary dependencies (including this parser)
```
git clone https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR nomad
git submodule update --init
pip install -r requirements.txt
./dependencies.sh -e
```

To run the parser:
```
cd nomad/dependencies/parser/photoemission
python -m photoemissionparser <test_file>
```

## Docs

[metainfo](https://metainfo.nomad-coe.eu/nomadmetainfo_public/archive.html)

[nomad@fairdi, tmp.](http://enc-staging-nomad.esc.rzg.mpg.de/fairdi/nomad/migration/docs)
