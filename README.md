# parser-skeleton

## About

This is not a real parser, its a skeleton for parsers. To write you own parsers, its
best to fork this skeleton and use it as a template.

## Setup and run example

We are currently targeting Python 3.6. Some nomad dependencies might still have problems
with 3.7++. It will definitely not work with 2.x.

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

Fork the this project, e.g. [gitlab](https://gitlab.mpcdf.mpg.de/nomad-lab/parser-skeleton).
Rename your fork in its settings/advanced and move it to the nomad-lab namespace.

Add your parser to the nomad project on a separate branch:
```
git checkout -b your-parser-name
git submodule add https://gitlab.mpcdf.mpg.de/nomad-lab/parser-your-parser-name dependencies/parsers/your-parser-name
```

Do the necessary changes:
- [setup.py](setup.py): Change the project metadata
- [skeletonparser](skeletonparser): Change the directory name
- [skeletonparser/__init__.py](skeletonparser/__init__.py): Implement your parser, change the class names
- [skeletonparser/__main__.py](skeletonparser/__main__.py): Change the module/class names
- [skeletonparser/skeleton.nomadmetainfo.json](skeletonparser/skeleton.nomadmetainfo.json): Change the name, add your metadata definitions.
- [README.md](README.md): Change this readme accordingly.


To run the parser:
```
cd nomad/dependencies/parsers/your-parsername
python -m your-parser-pythonpackage <test_file>
```

## Docs

[metainfo](https://metainfo.nomad-coe.eu/nomadmetainfo_public/archive.html)

[nomad@fairdi, tmp.](http://labdev-nomad.esc.rzg.mpg.de/fairdi/nomad/latest/docs)

## FAQ

For any questions, please open issues (regarding parser development and using this skeleton)
in this [parser-skeleton project](https://gitlab.mpcdf.mpg.de/nomad-lab/parser-skeleton/issues).
We will compile a FAQ from your issues.
