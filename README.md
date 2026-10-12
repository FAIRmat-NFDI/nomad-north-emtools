[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![](https://github.com/FAIRmat-NFDI/nomad-north-emtools/actions/workflows/actions.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/nomad-north-emtools/actions/workflows/publish.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/nomad-north-emtools/actions/workflows/mkdocs-deploy.yml/badge.svg)
![](https://img.shields.io/pypi/pyversions/nomad-north-emtools)
![](https://img.shields.io/pypi/l/nomad-north-emtools)
![](https://img.shields.io/pypi/v/nomad-north-emtools)
[![DOI with Zenodo](https://img.shields.io/badge/DOI-10.5281/zenodo.20051340-1073c8?labelColor=000000)](https://doi.org/10.5281/zenodo.20051340)

# nomad-north-emtools

A NOMAD NORTH plugin for analysis of electron microscopy data adding [HyperSpy](https://hyperspy.org/) (a Python library for multi-dimensional data analysis, widely used for electron microscopy spectroscopy and imaging data) together with [RosettaSciIO](https://hyperspy.org/rosettasciio/) (HyperSpy's companion I/O library, covering many microscopy-specific file formats).
The environment is registered as its own Jupyter kernel (`emtools`) and activated automatically in new terminals.

This `nomad` plugin was generated with `Cookiecutter` along with `@nomad`'s [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin) template.

## Adding this plugin to NOMAD

Currently, NOMAD has two distinct flavors that are relevant depending on your role as an user:

1. [A NOMAD Oasis](#adding-this-plugin-in-your-nomad-oasis): any user with a NOMAD Oasis instance.
2. [Local NOMAD installation and the source code of NOMAD](#adding-this-plugin-in-your-local-nomad-installation-and-the-source-code-of-nomad): internal developers.

### Adding this plugin in your NOMAD Oasis

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

### Adding this plugin in your local NOMAD installation and the source code of NOMAD

We now recommend using the dedicated [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev) repository to simplify the process. Please refer to that repository for detailed instructions.

## Publish note

In the [GitHub actions workflow](./.github/workflows/publish.yml) for publishing the nomad-north-emtools plugin to PyPI, we commented out the `deploy` job . If you want to publish the plugin to `PyPI`, you need to set up your project in `PyPI`. There are several online tutorials on publishing a Python package to PyPI, e.g., [How to Publish a Python Package to PyPI](https://realpython.com/pypi-publish-python-package/). After that, you can uncomment the `deploy` job in the workflow file and push the changes to GitHub. The workflow will be triggered and the package will be published to `PyPI` when you create a new release on GitHub.
In our Python package publishing workflow, before building the package, we update the image tag in the [NORTHTool](./src/nomad_north_emtools/north_tools/__init__.py) entry point to the latest release version of the image (e.g., `v0.1.2`), and then publish the package to PyPI.

However, the updated image tag in `NORTHTool` is not pushed back to the GitHub repository. Therefore, the image tag in the GitHub repository always remains set to `main`, even when you check out a specific release tag. For this reason, we recommend installing the plugin from [PyPI](https://pypi.org/), where the entry point always contains the correct image tag corresponding to the release.

If you download a ZIP file of a specific release from GitHub, the image tag in the entry point will still be set to `main`, which is not correct.In that case, you can either manually update the image tag in the entry point to the correct release version (e.g., `v0.1.2`), or install the plugin directly from PyPI.

### Template update

We use [`cruft`](https://github.com/cruft/cruft) to update the project based on template changes. To run the check for updates locally, run `cruft update` in the root of the project. More details see the instructions on [`cruft` website](https://cruft.github.io/cruft/#updating-a-project).

## Main contributors

| Name | E-mail     |
|------|------------|
| Markus Kühbach | [markus.kuehbach@physik.hu-berlin.de](mailto:markus.kuehbach@physik.hu-berlin.de)
