# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixgenerics(RPackage):
    """S4 Generic Summary Statistic Functions that Operate on Matrix-Like
    Objects.

    S4 generic functions modeled after the 'matrixStats' API for alternative
    matrix implementations. Packages with alternative matrix implementation can
    depend on this package and implement the generic functions that are defined
    here for a useful set of row and column summary statistics. Other package
    developers can import this package and handle a different matrix
    implementations without worrying about incompatibilities."""

    bioc = "MatrixGenerics"version("1.8.1", commit="a4a21089e9f78275dd4a6f0df0c4b6b45c4650c7")
    version("1.8.0", commit="e4cc34d53bcfb9a5914afd79fda31ecd5037a47a")
    version("1.6.0", commit="4588a60e5cc691424c17faa281bdd7d99d83ec34")
    version("1.2.1", commit="abcc9ca0504e0b915cd7933a3169a8e9e5bd2fe9")
    version("1.20.0", commit="02c5112ebfcf018ceca144ccbfca1fef46d36a47")
    version("1.14.0", commit="9a52271933ef06a031479f0609fb4e8d8e77fbc1")
    version("1.12.0", commit="442fde27fdf18ee3460ea0258a74a847b2c99cf3")
    version("1.10.0", commit="6d9d907e8c4d1fc96a32160fb9f3ab805d6eb356")

    depends_on("r-matrixstats@1:", type=("build", "run"))
    depends_on("r-matrixstats@1.4.1:", type=("build", "run"), when="@1.20.0:")
