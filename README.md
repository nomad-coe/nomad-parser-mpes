# mpes-parser

## About

Multidimensional photoemission spectroscopy (MPES) experimental data parser for NOMAD-FAIR database.

## Description of files
The set of important files for the parser are explained in the following,
- [mpesparser](mpesnparser): Change the directory name, i.e. python package name (no uppercases, no `_` please)
- [mpesparser/__init__.py](skeletonparser/__init__.py): Parser module initialization.
- [mpesparser/__main__.py](skeletonparser/__main__.py): Parser module main run file.
- [mpesparser/mpes.nomadmetainfo.json](mpesparser/mpes.nomadmetainfo.json): MPES metadata definitions.

To run the parser:
```
cd nomad/dependencies/parsers/parser-mpes
python -m parser-mpes tests/mpes.metadata.json
```
