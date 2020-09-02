#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()


def get_requirements(requirements_file="requirements.txt"):
    """Get the contents of a file listing the requirements.
    :arg requirements_file: path to a requirements file
    :type requirements_file: string
    :returns: the list of requirements, or an empty list if
              `requirements_file` could not be opened or read
    :return type: list
    """

    try:
        lines = open(requirements_file).readlines()
    except FileNotFoundError:
        lines = []
    dependencies = []
    for line in lines:
        maybe_dep = line.strip()
        if maybe_dep.startswith("#"):
            # Skip pure comment lines
            continue
        if maybe_dep.startswith("git+"):
            # VCS reference for dev purposes, expect a trailing comment
            # with the normal requirement
            __, __, maybe_dep = maybe_dep.rpartition("#")
        else:
            # Ignore any trailing comment
            maybe_dep, __, __ = maybe_dep.partition("#")
        # Remove any whitespace and assume non-empty results are dependencies
        maybe_dep = maybe_dep.strip()
        if maybe_dep:
            dependencies.append(maybe_dep)
    return dependencies


setup(
    author="Michal Konečný",
    author_email="michal.konecny@packetseekers.eu",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Interactive map of the Fedora Infrastructure applications ",
    entry_points={
        "console_scripts": [
            "fedora_infra_map=fedora_infra_map.cli:main",
        ],
    },
    install_requires=get_requirements(),
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fedora_infra_map",
    name="fedora_infra_map",
    packages=find_packages(include=["fedora_infra_map", "fedora_infra_map.*"]),
    test_suite="tests",
    tests_require=get_requirements("requirements_test.txt"),
    url="https://github.com/zlopez/fedora_infra_map",
    version="0.1.0",
    zip_safe=False,
)
