# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharedobject(RPackage):
    """Sharing R objects across multiple R processes without memory duplication

    This package is developed for facilitating parallel computing in R. It is capable to create an R object in the shared memory space and share the data across multiple R processes. It avoids the overhead of memory dulplication and data transfer, which make sharing big data object across many clusters possible.
    """

    bioc = "SharedObject"

    version("1.22.0", commit="4beeb17fdf8e8e50fc2c16e83be162f79e8ad11b")
    version("1.16.0", commit="bfa7f71040ef41df18e4ede0d692df5eff5687cd")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
