# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialde(RPackage):
    """R wrapper for SpatialDE

    SpatialDE is a method to find spatially variable genes (SVG) from spatial transcriptomics data. This package provides wrappers to use the Python SpatialDE library in R, using reticulate and basilisk.
    """

    homepage = "https://github.com/sales-lab/spatialDE"
    bioc = "spatialDE"

    version("1.14.1", commit="205de11bc541782b4561b84b837449ae54a20fee")
    version("1.8.1", commit="2f7926f5e1d6b9d8b53efe92fbc779694a70f9d5")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-basilisk@1.9.10:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
