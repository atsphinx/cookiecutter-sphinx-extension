"""{{ cookiecutter.description }}."""

from sphinx.application import Sphinx

__version__ = "{{ cookiecutter.version }}"


def setup(app: Sphinx):  # noqa: D103
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
