# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsclust(RPackage):
    """Feature-based variance-sensitive quantitative clustering

    Feature-based variance-sensitive clustering of omics data. Optimizes cluster assignment by taking into account individual feature variance. Includes several modules for statistical testing, clustering and enrichment analysis.
    """

    bioc = "vsclust"

    version("1.10.0", commit="635720b3fe4a852a82fdcbb81b405186ccf9e6a0")
    version("1.4.0", commit="c49bf51093e571710ac2b7c680881f0e4e431c83")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
