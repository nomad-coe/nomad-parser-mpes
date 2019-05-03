# mpesparser
@author = R. Patrick Xian (xian@fhi-berlin.mpg.de)

## About

Multidimensional photoemission spectroscopy (MPES) experimental data parser for NOMAD-FAIR database.

## Description of files
The set of important files for the parser are explained in the following,
- [mpesparser](mpesnparser): Main folder of the parser.
- [mpesparser/__init__.py](skeletonparser/__init__.py): Parser module initialization code.
- [mpesparser/__main__.py](skeletonparser/__main__.py): Parser module run file.
- [mpesparser/mpes.nomadmetainfo.json](mpesparser/mpes.nomadmetainfo.json): MPES metadata definitions.

To run the parser:
```
cd nomad/dependencies/parsers/parser-mpes
python -m parser-mpes tests/mpes.metadata.json
```
