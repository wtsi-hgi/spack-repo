# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEqtlSumstatsFileValidator(PythonPackage):
    """A file validator for validating eQTL summary statistics TSV files prior to conversion to HDF5. The validator uses pandas_schema."""

    homepage = "https://github.com/eQTL-Catalogue/eQTL-sumstats-file-validator"
    git = "https://github.com/eQTL-Catalogue/eQTL-sumstats-file-validator.git"

    version("2020-04-14", commit="66d66db27ddd8b002e39b2a28d4dc271dbd01498")

    depends_on("py-atomicwrites@1.3.0:", type=("build", "run"))
    depends_on("py-attrs@19.1.0:", type=("build", "run"))
    depends_on("py-importlib-metadata@0.19:", type=("build", "run"))
    depends_on("py-more-itertools@7.2.0:", type=("build", "run"))
    depends_on("py-numpy@1.17.0:", type=("build", "run"))
    depends_on("py-packaging@19.1:", type=("build", "run"))
    depends_on("py-pandas@0.25.0:", type=("build", "run"))
    depends_on("py-pandas-schema@0.3.4:", type=("build", "run"))
    depends_on("py-pluggy@0.12.0:", type=("build", "run"))
    depends_on("py-py@1.8.0:", type=("build", "run"))
    depends_on("py-pyparsing@2.4.2:", type=("build", "run"))
    depends_on("py-pytest@5.0.1:", type=("build", "run"))
    depends_on("py-python-dateutil@2.8.0:", type=("build", "run"))
    depends_on("py-pytz@2019.2:", type=("build", "run"))
    depends_on("py-six@1.12.0:", type=("build", "run"))
    depends_on("py-wcwidth@0.1.7:", type=("build", "run"))
    depends_on("py-zipp@0.5.2:", type=("build", "run"))
