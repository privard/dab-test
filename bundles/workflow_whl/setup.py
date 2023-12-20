from setuptools import setup, find_packages

import sys
sys.path.append('./workflow_whl')

import datetime
import workflow_whl

setup(
    name="workflow_whl",
    # We use timestamp as Local version identifier (https://peps.python.org/pep-0440/#local-version-identifiers.)
    # to ensure that changes to wheel package are picked up when used on all-purpose clusters
    version=workflow_whl.__version__ + "+" + datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S"),
    description="wheel file based on workflow_whl/src",
    packages=find_packages(where='.'),
    entry_points={
        "packages": [
            "main=workflow_whl.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools",
        # Adding the shared_lib dependency here also fails because DBR doesn't know
        # where to find it at install time
        # .i.e. ERROR: No matching distribution found for shared-lib
        # "shared_lib"
    ],
)
