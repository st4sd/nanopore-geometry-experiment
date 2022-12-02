# © Copyright IBM Corp. 2022 All Rights Reserved

import os


def get_res_data(directory_path):
    """
    Get pore diameter data from the .res file

    Parameters
    ----------
    directory_path: str
        Path to the directory that holds the Zeo.res file

    Returns
    -------
    res_dicts: list
        List of dictionaries of pore diameter data in Angstrom
    """

    # Open output file
    with open(os.path.join(directory_path, 'Zeo.res'), 'r') as res_file:
        res_data = res_file.readlines()

    # Get acessible surface area data
    splitted_data = res_data[0].split()

    # Build a list with dictionaries containing the pore diameter data
    res_dicts = [{'name': 'D_is',   'value': float(splitted_data[1]),   'unit': 'Angstrom'},
                 {'name': 'D_fs',   'value': float(splitted_data[2]),   'unit': 'Angstrom'},
                 {'name': 'D_isfs', 'value': float(splitted_data[3]),   'unit': 'Angstrom'}]

    return res_dicts


def get_sa_data(directory_path):
    """
    Get surface area data from .sa file.

    Parameters
    ----------
    directory_path: str
        Path to the directory that holds the Zeo.sa file

    Returns
    -------
    sa_dicts: list
        List of dictionaries of surface area data
    """

    # Open output file
    with open(os.path.join(directory_path, 'Zeo.sa'), 'r') as sa_file:
        sa_data = sa_file.readlines()

    # Get acessible surface area data
    splitted_data = sa_data[0].split()

    # Build a list with dictionaries containing the accessible surface area data
    sa_dicts = [{'name': 'ASA_m^2/cm^3',    'value': float(splitted_data[9]),   'unit': 'm^2/cm^3'},
                {'name': 'ASA_m^2/g',       'value': float(splitted_data[11]),  'unit': 'm^2/g'},
                {'name': 'NASA_m^2/cm^3',   'value': float(splitted_data[15]),  'unit': 'm^2/cm^3'},
                {'name': 'NASA_m^2/g',      'value': float(splitted_data[17]),  'unit': 'm^2/g'}]

    return sa_dicts


def get_vol_data(directory_path):
    """
    Get pore volume data from .vol file.

    Parameters
    ----------
    directory_path: str
        Path to the directory that holds the Zeo.vol file

    Returns
    -------
    vol_dicts: list
        List of dictionaries of volume data
    """

    # Open output file
    with open(os.path.join(directory_path, 'Zeo.vol'), 'r') as vol_file:
        vol_data = vol_file.readlines()

    # Get acessible volume data
    splitted_data = vol_data[0].split()

    # Get the number of pockets
    n_pockets = int(vol_data[2].split()[1])

    # Build a list with dictionaries containing the pore volume area data
    vol_dicts = [
        {'name': 'Unitcell_volume',     'value': float(splitted_data[3]),   'unit': 'Angstrom^3'},
        {'name': 'Density',             'value': float(splitted_data[5]),   'unit': 'g/cm^3'},
        {'name': 'AV_Volume_fraction',  'value': float(splitted_data[9]),   'unit': ''},
        {'name': 'AV_cm^3/g',           'value': float(splitted_data[11]),  'unit': 'cm^3/g'},
        {'name': 'NAV_Volume_fraction', 'value': float(splitted_data[15]),  'unit': ''},
        {'name': 'NAV_cm^3/g',          'value': float(splitted_data[17]),  'unit': 'cm^3/g'},
        {'name': 'n_pockets',           'value': n_pockets,                 'unit': ''}
    ]

    return vol_dicts
