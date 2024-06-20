#!/usr/bin/env python3

# © Copyright IBM Corp. 2022 All Rights Reserved
# SPDX-License-Identifier: Apache2.0

import argparse
import os
import json

import requests


def _url(path):
    return f'http://database-api.{os.environ["INGRESS_SUBDOMAIN"]}' + path


def get_objectIDByNameAndSource(materialName, materialSource):
    """
    Get the MongoDB objectID for a material by its name and source.
    """
    url = _url(f'/materials?name={materialName}&source={materialSource}')
    response = requests.get(url).json()
    materials = response["materials"]
    objectID = materials[0]['_id']
    return objectID


def post_geomProp(id, name, value, unit):
    """
    Post a new geometric property to the database.
    """
    url = _url(f'/materials/{id}/geometric-properties')
    print(url)
    geomProp = {'name': name,
                'value': value,
                'unit': unit}
    return requests.post(url, json=geomProp)


def put_geomProp(id, name, value, unit):
    """
    Put a new geometric property to the database.
    """
    url = _url(f'/materials/{id}/geometric-properties')
    geomProp = {'name': name,
                'value': value,
                'unit': unit}
    return requests.put(url, json=geomProp)


def main():
    if (os.environ.get("INGRESS_SUBDOMAIN") is None or os.environ.get("INGRESS_SUBDOMAIN") == ""
            or os.environ.get("INGRESS_SUBDOMAIN") == "${INGRESS}"):
        ingress_subdomain = False
    else:
        ingress_subdomain = True

    # Required parameters
    parser = argparse.ArgumentParser(description='Writing geometric analyses to database.')
    parser.add_argument('directory',
                        type=str,
                        action='store',
                        metavar='DIRECTORY',
                        help='Directory for storing input/output files.')
    parser.add_argument('--FrameworkName',
                        type=str,
                        required=True,
                        action='store',
                        metavar='FRAMEWORK_NAME',
                        help='Name of the CIF file describing the nanoporous material structure.')
    parser.add_argument('--FrameworkSource',
                        type=str,
                        required=True,
                        action='store',
                        metavar='FRAMEWORK_SOURCE',
                        choices=['local',
                                 'CSD',
                                 'hMOF',
                                 'BWDB',
                                 'BW20K',
                                 'ARABG',
                                 'CoRE2019',
                                 'CoRE_DDEC',
                                 'CURATED-COF',
                                 'baburin_2008',
                                 'simperler_2005',
                                 'database_zeolite_structures'],
                        help='Source of the CIF file describing the nanoporous material structure.')
    arg = parser.parse_args()

    # Build the path to the geometric file json
    geometric_file = os.path.join(arg.directory, 'geometricProperties.json')

    print(f'Material name is {arg.FrameworkName} and material source is {arg.FrameworkSource}.')

    if ingress_subdomain:
        # Get MongoDB objectIDs for the material
        mongoObjectID = get_objectIDByNameAndSource(arg.FrameworkName, arg.FrameworkSource)

        print("Mongo objectID is :", mongoObjectID)

    # Read the geometric properties from the json file
    with open(geometric_file, 'r') as f:
        geometric_data = json.load(f)

    if ingress_subdomain:
        # Write the geometric properties to the database
        for property in geometric_data['geometricProperties']:
            response = post_geomProp(id=mongoObjectID,
                                     name=property['name'],
                                     value=property['value'],
                                     unit=property['unit'])
            if response.status_code == 403:
                response = put_geomProp(id=mongoObjectID,
                                        name=property['name'],
                                        value=property['value'],
                                        unit=property['unit'])
            print(response.json(), '\n')


if __name__ == '__main__':
    main()
