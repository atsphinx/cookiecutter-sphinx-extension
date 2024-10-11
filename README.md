# cookiecutter-sphinx-extension

My cookiecutter template to generate Sphinx extension prefixed `atsphinx`.

## About generated project

- PyPI's package name has `atsphinx-` as prefix.
- Package is namespaced package for `atsphinx.`.
- Manage project data with Rye.
- Manage target bumpversion with age-cli.
- Included documentation template and tests.

## Usage

This requirements Git and cookiecutter.

```console
cookiecutter https://github.com/atsphinx/cookiecutter-sphinx-extension
```

For me

```
uvx cookiecutter -o .. --no-input . requires_python='3.9' \
  project_basename='NAME' description='DESCRIPTION'
```
