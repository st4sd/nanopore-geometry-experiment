#!/usr/bin/env sh
cd $(dirname ${0})/..

docker_like_location=""
if ! which docker >/dev/null; then
    echo "The docker command is not available on this system, will try to use podman" >&2

    if location=$(which podman); then 
        docker_like_location="--dockerExecutableOverride=${location}"
        echo "Podman located at ${location}" >&2
    else
        echo "No docker or podman command on this system - aborting" >&2
        exit 2
    fi
fi

# Run experiment
echo "Executing the experiment ..." >&2
elaunch.py --failSafeDelays=no ${docker_like_location} -l40 \
    --instanceName nanopore-geometry-experiment \
    --manifest manifest.yaml \
    --input docker-example/cif_files.dat \
    --platform docker conf/flowir_package.yaml

# See outputs of experiment
echo "\n\nMeasured properties are:" >&2
output_dir=$(ls -td nanopore-geometry-experiment*.instance | head -1)
cat "${output_dir}/output/properties.csv"
