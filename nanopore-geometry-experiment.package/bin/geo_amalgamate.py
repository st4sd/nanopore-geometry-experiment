#!/usr/bin/env python

# © Copyright IBM Corp. 2020 All Rights Reserved
# SPDX-License-Identifier: Apache2.0

import argparse
import json
import os

import modules.parse_zeopp as zeopp

# Required parameters
parser = argparse.ArgumentParser(description='Amalgamating geometric descriptors.')
parser.add_argument('directory',
                    type=str,
                    action='store',
                    metavar='DIRECTORY',
                    help='Directory for storing input/output files.')
arg = parser.parse_args()

# Build the geometric dictionary
geometric_dict = {'geometricProperties': []}

# Get pore diameter data from the .res file
res_dicts = zeopp.get_res_data(arg.directory)
geometric_dict['geometricProperties'] += res_dicts

# Get accessible surface area data from .sa file
sa_dicts = zeopp.get_sa_data(arg.directory)
geometric_dict['geometricProperties'] += sa_dicts

# Get pore volume data from .vol file
vol_dicts = zeopp.get_vol_data(arg.directory)
geometric_dict['geometricProperties'] += vol_dicts

# Dump the geometric dictionary to a json file
with open(os.path.join(arg.directory, 'geometricProperties.json'), mode='w') as f:
    json.dump(geometric_dict, f, indent=2)
