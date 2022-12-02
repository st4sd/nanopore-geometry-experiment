#!/usr/bin/env bash

# © Copyright IBM Corp. 2022 All Rights Reserved

# Parse input parameters
while getopts p:o:n: flag
do
    case "${flag}" in
        p) ProbeRadius=${OPTARG};;
        o) OutputFolder=${OPTARG};;
        n) FrameworkName=${OPTARG};;
    esac
done

echo -e "\nDecompressing CIF files..."
tar --no-overwrite-dir -xvzf cif.tgz -C ${OutputFolder} && cd ${OutputFolder}

echo -e "\nCalculating pore size..."
network -ha -res Zeo.res ${FrameworkName}.cif

echo -e "\nCalculating acessible surface area..."
network -ha -sa ${ProbeRadius} ${ProbeRadius} 20000 Zeo.sa ${FrameworkName}.cif

echo -e "\nCalculating pore volume..."
network -ha -vol ${ProbeRadius} ${ProbeRadius} 200000 Zeo.vol ${FrameworkName}.cif
