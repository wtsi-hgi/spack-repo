# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimlr(RPackage):
    """Single-cell Interpretation via Multi-kernel LeaRning (SIMLR)

    Single-cell RNA-seq technologies enable high throughput gene expression measurement of individual cells, and allow the discovery of heterogeneity within cell populations. Measurement of cell-to-cell gene expression similarity is critical for the identification, visualization and analysis of cell populations. However, single-cell data introduce challenges to conventional measures of gene expression similarity because of the high level of noise, outliers and dropouts. We develop a novel similarity-learning framework, SIMLR (Single-cell Interpretation via Multi-kernel LeaRning), which learns an appropriate distance metric from the data for dimension reduction, clustering and visualization.
    """

    homepage = "https://github.com/BatzoglouLabSU/SIMLR"
    bioc = "SIMLR"

    version("1.34.0", commit="26ba6d89f14863708b72a99b2617df2a2d8f03b9")
    version("1.28.0", commit="e833718b068304badc3d417e498f72733fa77a72")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
    depends_on("r-rcppannoy", type=("build", "run"))
    depends_on("r-rspectra", type=("build", "run"))
