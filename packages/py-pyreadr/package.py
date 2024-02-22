# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyreadr(PythonPackage):
    """A python package to read and write R RData and Rds files into/from pandas dataframes. It does not need to have R or other external dependencies installed."""

    homepage = "https://github.com/ofajardo/pyreadr"
    pypi = "pyreadr/pyreadr-0.4.4.tar.gz"

    version("0.4.4", sha256="690a6d87f25b6b211bad0d73fe0c9be87718e62329b142d835eadd951982c6ad")

    depends_on("python@3.9.9")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.29.36", type="build")
    depends_on("py-wheel", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")
