#!/usr/bin/env python3

# © Copyright IBM Corp. 2022 All Rights Reserved
# SPDX-License-Identifier: Apache2.0

import argparse
import os
import tarfile
import shutil

# Required parameters
parser = argparse.ArgumentParser(description='Aggregating geometric output to compressed file.')
parser.add_argument('--FrameworkName',
                    type=str,
                    required=True,
                    action='store',
                    nargs='+',
                    metavar='FRAMEWORK_NAME',
                    help='Name of the CIF file describing the nanoporous material structure.')
parser.add_argument('--OutputFolders',
                    type=str,
                    required=True,
                    action='store',
                    nargs='+',
                    metavar='OUTPUT_FOLDERS',
                    help='Directory for storing JSON output files.')
arg = parser.parse_args()

print(f'Aggregating geometric output json files from {arg.FrameworkName}, {arg.OutputFolders}.')

# Copy geometricProperties.json from all given Output Folders to AggregateGeometry folder
for i in range(len(arg.OutputFolders)):
    src = os.path.join(arg.OutputFolders[i], 'geometricProperties.json')
    shutil.copyfile(src, arg.FrameworkName[i] + '-geometry.json')

# Compress to create geometry.tgz
with tarfile.open('geometry.tgz', 'w') as tar:
    for file in os.listdir():
        if file.endswith('.json'):
            tar.add(file)
