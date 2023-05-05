"""Standard tests."""
from io import StringIO

import pytest
from docutils import nodes
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    """Test to pass."""
