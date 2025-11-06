# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvsusier(RPackage):
    """Multivariate Sum of Single Effects Regression

    Implements a multivariate generalization of the "Sum of Single Effects"
    (SuSiE) model for variable selection in multivariate linear regression.
    """

    homepage = "https://github.com/stephenslab/mvsusieR"
    url = "https://github.com/stephenslab/mvsusieR/archive/refs/tags/0.1.8.tar.gz"
    git = "https://github.com/stephenslab/mvsusieR.git"

    license("BSD-3-Clause")

    version("0.1.8", sha256="fff3d75b1e579ce7c772255d8d37bd574588613e90c1680e93fdd0c683f6cd5a")
    version("0.1.7", sha256="7bf074af239d2b7a3cdb63809a498ada36d10306db9aa46d2b6b2305ad1121f1")
    version("0.1.6", sha256="e1c724222c783ea9d0ecf1d5df8b408cbf864967eaa1e4defe95353dd283cd7f")
    version("0.1.0", sha256="a7b4fd910013c9344ce7a1acd245b952ddfda456529303b2999e9a2c54df168e")

    depends_on("r@3.5.0:", type=("build", "run"))

    # Strong dependencies from DESCRIPTION Depends/Imports
    depends_on("r-mashr@0.2.43:", type=("build", "run"))
    depends_on("r-susier@0.10.1:", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-ashr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))

    # Suggested packages: include as standard dependencies per repo policy
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-pryr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-microbenchmark", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))

