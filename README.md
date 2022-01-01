[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
<!-- These are examples of badges you might also want to add to your README. Update the URLs accordingly.
[![Built Status](https://api.cirrus-ci.com/github/<USER>/crypto_01.svg?branch=main)](https://cirrus-ci.com/github/<USER>/crypto_01)
[![ReadTheDocs](https://readthedocs.org/projects/crypto_01/badge/?version=latest)](https://crypto_01.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/crypto_01/main.svg)](https://coveralls.io/r/<USER>/crypto_01)
[![PyPI-Server](https://img.shields.io/pypi/v/crypto_01.svg)](https://pypi.org/project/crypto_01/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/crypto_01.svg)](https://anaconda.org/conda-forge/crypto_01)
[![Monthly Downloads](https://pepy.tech/badge/crypto_01/month)](https://pepy.tech/project/crypto_01)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/crypto_01)
-->
---
![Alt text](https://github.com/KaissonFerreira/crypto/blob/16a3c54253ad4632cb4c4e323e442ef89c5b7619/reports/figures/cripto.png)
---
# crypto

> This project aims to perform the ETL of some cryptocurrencies on the Binance platform and load them into Big Query, and later analyze them with predictive models.



## Installation

In order to set up the necessary environment:

1. review and uncomment what you need in `environment.yml` and create an environment `crypto` with the help of [conda]:
   ```
   conda env create -f environment.yml
   ```
2. activate the new environment with:
   ```
   conda activate crypto
   ```

> **_NOTE:_**  The conda environment will have crypto_01 installed in editable mode.
> Some changes, e.g. in `setup.cfg`, might require you to run `pip install -e .` again.


Optional and needed only once after `git clone`:

3. install several [pre-commit] git hooks with:
   ```bash
   pre-commit install
   # You might also want to run `pre-commit autoupdate`
   ```
   and checkout the configuration under `.pre-commit-config.yaml`.
   The `-n, --no-verify` flag of `git commit` can be used to deactivate pre-commit hooks temporarily.

4. install [nbstripout] git hooks to remove the output cells of committed notebooks with:
   ```bash
   nbstripout --install --attributes notebooks/.gitattributes
   ```
   This is useful to avoid large diffs due to plots in your notebooks.
   A simple `nbstripout --uninstall` will revert these changes.


Then take a look into the `scripts` and `notebooks` folders.

## Dependency Management & Reproducibility

1. Always keep your abstract (unpinned) dependencies updated in `environment.yml` and eventually
   in `setup.cfg` if you want to ship and install your package via `pip` later on.
2. Create concrete dependencies as `environment.lock.yml` for the exact reproduction of your
   environment with:
   ```bash
   conda env export -n crypto -f environment.lock.yml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yml` using:
   ```bash
   conda env update -f environment.lock.yml --prune
   ```
## Project Organization

```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── Dockerfile              <- Build a docker container with `docker build .`.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── ETL                     <- Run ETL for cryptocurrencies.
|  └── logs                   <- Logs of the ETL dailly.
│  ├── src
│     ├── config.py              <- Script for the configurations
│     ├── extract.py             <- Script for the extraction of data.
│     ├── loading.py             <- Script for the loading data in Base Data (Big Query or MySQL).
│     ├── pipeline.py            <- Script for the Pipeline of the data.
│     └── transform.py           <- Script for the trasfortion data.
├── code
|  ├── configs                <- Directory for configurations of model & application.
|  ├── data
│     ├── external            <- Data from third party sources.
│     ├── interim             <- Intermediate data that has been transformed.
│     ├── processed           <- The final, canonical data sets for modeling.
│     └── raw                 <- The original, immutable data dump.
|  ├── models                 <- Trained and serialized models, model predictions,
|  │                                or model summaries.
│  ├── notebooks              <- Jupyter notebooks. Naming convention is a number (for
│  │                                ordering), the creator's initials and a description,
│  │                                e.g. `1.0-fw-initial-data-exploration`.
│  ├── src
│  │   └── crypto_01           <- Actual Python package where the main functionality goes.
│  ├── tests                   <- Unit tests which can be run with `pytest`.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yml         <- The conda environment file for reproducibility.
├── pyproject.toml          <- Build configuration. Don't change! Use `pip install -e .`
│                              to install for development or to build `tox -e build`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── setup.cfg               <- Declarative configuration of your project.
├── setup.py                <- [DEPRECATED] Use `python setup.py develop` to install for
│                              development or `python setup.py bdist_wheel` to build.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```

<!-- pyscaffold-notes -->

## Note

This project has been set up using [PyScaffold] 4.1.1 and the [dsproject extension] 0.7.1.

[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[PyScaffold]: https://pyscaffold.org/
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
