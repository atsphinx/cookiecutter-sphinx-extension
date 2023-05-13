# noqa: D100
from {{ cookiecutter.package_fullname }} import __version__ as version

# -- Project information
project = "{{ cookiecutter.project_name }}"
copyright = "2023, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"
release = version

# -- General configuration
extensions = [
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
