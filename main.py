"""Run script for cookiecutter."""

import argparse
import json
from pathlib import Path

from cookiecutter.main import cookiecutter

root = Path(__file__).parent

base_context = json.loads((root / "cookiecutter.json").read_text())

parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, nargs=1)
parser.add_argument("-d", "--description")


def main(args: argparse.Namespace):
    """"""
    context = {
        "project_basename": args.name,
        "description": args.description or base_context["description"],
        "workspace_python": "3.11",
    }
    cookiecutter(
        template=str(root),
        no_input=True,
        extra_context=context,
        output_dir=str(root.parent),
    )


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
