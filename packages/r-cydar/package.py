# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCydar(RPackage):
    """Using Mass Cytometry for Differential Abundance Analyses

    Identifies differentially abundant populations between samples and groups in mass cytometry data. Provides methods for counting cells into hyperspheres, controlling the spatial false discovery rate, and visualizing changes in abundance in the high-dimensional marker space.
    """

    bioc = "cydar"

    version("1.32.1", commit="7c6a4c8df2956dbcb6893eb5518895c54d6f8fa6")
    version("1.26.0", commit="0191ed4f866cf42f61574df80c26cd5c66f2da37")

    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocneighbors", type=("build", "run"))
