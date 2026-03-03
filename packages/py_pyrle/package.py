# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyrle(PythonPackage):
    """Run length arithmetic in Python using Cython. Inspired by the Rle class in R's S4Vectors."""

    homepage = "https://github.com/pyranges/pyrle"
    pypi = "pyrle/pyrle-0.0.39.tar.gz"

    version("0.0.39", sha256="1be4be7814d3941db907aaf19f311bd46a407244316cadbf4b73109685c055c5")

    depends_on("py-cython", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
