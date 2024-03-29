# Nanopore Geometry Experiment

Automated virtual experiment that calculates geometric properties of nanoporous materials using the Zeo++ software package.

## Quick links

- [Launching the virtual experiment](#launching-the-virtual-experiment)
- [Using custom database of CIF files](#using-custom-database-of-cif-files)
- [Help and Support](#help-and-support)
- [Contributing](#contributing)
- [License](#license)

## Launching the virtual experiment

First you need to import the virtual experiment in your ST4SD registry [from the global ST4SD registry](https://st4sd.github.io/overview/using-the-virtual-experiments-registry-ui). You will then be able to start the parameterised package `nanopore-geometry-experiment` in your private ST4SD registry (see [example notebook](nanopore-geometry-experiment.ipynb)).

## Using custom database of CIF files

You may download the CIF files of your choosing to a PVC inside your OpenShift cluster (below we use the name `nanopore-database-pvc`), mount it as a volume and ask the virtual experiment instance to use the contents of the PVC as the contents of the `nanopore-database` application-dependency. You will also need to remove the line related to `nanopore-database` from the `manifest.yaml` to enable the use of the PVC.

```Python
file_names = [""]
payload = {
  "volumes": [{
        "type": {"persistentVolumeClaim": "nanopore-database-pvc"},
        "applicationDependency": "nanopore-database"
    }],
  # other fields
}
rest_uid = api.api_experiment_start("nanopore-geometry-experiment", payload)
```

**Note**: The [example notebook](nanopore-geometry-experiment.ipynb) shows a full example.

**Note**: You can also run a small scale experiment using docker/podman. See our example [here](docker-example/README.md).

## Help and Support

Please feel free to create an issue and alert the maintainers listed in the [MAINTAINERS.md](MAINTAINERS.md) page.

## Contributing

We always welcome external contributions. Please see our [guidance](CONTRIBUTING.md) for details on how to do so.

## License

This project is licensed under the Apache 2.0 license. Please [see details here](LICENSE.md).
