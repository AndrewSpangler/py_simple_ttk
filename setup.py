#!/usr/bin/env python

import os, sys, json
from os.path import join
from setuptools import setup
from generate_readme import generate_readme

if __name__ == "__main__":
    with open("build_config.json") as f:
        settings = json.load(f)

    def make_toml(tables: dict):
        toml = ""
        for t in tables:
            toml += f"[{t}]\n"
            # Get table dict and write it
            tab = tables[t]
            for l in tab:
                if isinstance(tab[l], str):
                    toml += f'{l} = "{tab[l]}"\n'
                else:
                    toml += f"{l} = {tab[l]}\n"
            toml += "\n"
        return toml.strip()

    data = {
        "build-system": {
            "requires": ["setuptools>=61.0"],
            "build-backend": "setuptools.build_meta",
        },
        "project": {
            "name": (name := settings["name"]),
            "version": settings["version"],
            "description": settings["description"],
            "readme": "README.md",
            "requires-python": ">=3.8",
            "classifiers": [
                "Development Status :: 1 - Planning",
                "Environment :: Console",
                "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                "Natural Language :: English",
                "Operating System :: OS Independent",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
            ],
            "dependencies": (requirements := settings["requirements"]),
            "keywords": [],
        },
        "project.urls": {
            '"Homepage"': settings["url"],
            '"Bug Tracker"': settings["url"] + "issues",
        },
    }

    root = os.path.abspath(os.path.dirname(__file__))

    # Regenerate pyproject.toml
    with open(join(root, "pyproject.toml"), "w+") as f:
        f.write(make_toml(data))

    # Regenerate README.md
    with open(join(root, "README.md"), "w+") as f:
        readme = generate_readme(data, settings["changelog"])
        f.write(readme)

    # Regenerate requirements.txt
    with open(join(root, "requirements.txt"), "w+") as f:
        f.writelines(requirements)

    setup(
        name=name,
        author_email=settings["email"],
        long_description=readme,
        package_dir={name: name},
        package_data={"": ["*"]},
        include_package_data=True,
    )
