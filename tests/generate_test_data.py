# Copyright 2016-2018 Markus Scheidgen
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import ase.data
import random
import time
import zipfile
import json
import sys


if __name__ == '__main__':

    count = int(sys.argv[1])
    zipfile_name = sys.argv[2]

    atoms = ase.data.chemical_symbols
    low_numbers_for_atoms = [1, 1, 2, 2, 2, 2, 2, 3, 3, 4]

    methods = ['human eye examination', 'optical microscopes', 'TEM', 'photonemission', 'spectroscopy']
    locations = ['FHI', 'HU Berlin', 'Desy', 'ACME']
    chemical_names = ['super gue', 'dilithium', 'unoptanium', 'graphene 2.0', 'ducktape']

    now = int(time.time())

    for i in range(0, count + 1):
        with zipfile.ZipFile(zipfile_name, 'w') as zf:
            formula = []
            for _ in range(0, random.choice(low_numbers_for_atoms)):
                formula.append('%s%d' % (random.choice(atoms), random.choice(low_numbers_for_atoms)))
            data = dict(
                type='skeleton experimental metadata format 1.0',
                location=random.choice(locations),
                method=random.choice(methods),
                date=time.strftime('%d.%M.%Y', time.localtime(random.uniform(0, now))),
                sample_chemical=random.choice(chemical_names),
                sample_formula=''.join(formula),
                sample_temp=random.uniform(0, 6000)
            )

            with zf.open('experiment_%d/data.json' % i, 'w') as f:
                f.write(bytes(json.dumps(data, indent=4), 'utf-8'))
