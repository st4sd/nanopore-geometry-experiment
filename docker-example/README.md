# Run nanopore-geometry-experiment using the Docker backend of ST4SD

## Prerequisites

1. A recent version of python 3 - [python 3.7+](https://www.python.org/downloads/)
2. The [docker](https://docs.docker.com/get-docker/) container runtime
3. The [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) command-line utility


## Instructions

You can try out the experiment on your laptop by:

1. creating a python virtual environment, activating it, and installing the python module `st4sd-runtime-core`
2. cloning this repository
3. launching the experiment


For example:

```bash
#!/usr/bin/env sh

# Download virtual experiment
git clone https://github.com/st4sd/nanopore-geometry-experiment.git

# Setup ST4SD runtime-core
python3 -m venv --copies venv
. venv/bin/activate
python3 -m pip install "st4sd-runtime-core"

# Run experiment
./nanopore-geometry-experiment/docker-example/run.sh
```

**Note**: Make sure you run the `git clone` command in a directory that `docker` (or `podman`) can mount later when you execute the experiment.