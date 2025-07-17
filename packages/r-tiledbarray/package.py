# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiledbarray(RPackage):
    """Using TileDB as a DelayedArray Backend

    Implements a DelayedArray backend for reading and writing dense or sparse arrays in the TileDB format. The resulting TileDBArrays are compatible with all Bioconductor pipelines that can accept DelayedArray instances.
    """

    homepage = "https://github.com/LTLA/TileDBArray"
    bioc = "TileDBArray"

    version("1.18.0", commit="24d61dd61fffba2b2b6f8b05df35ca9b4004dd00")
    version("1.12.0", commit="c9a0eaf0cb6e9ca579f2e40bdcbe8c556a32d754")

    depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-tiledb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
