# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowsc(RPackage):
    """Simulation, power evaluation, and sample size recommendation for single cell RNA-seq

    Determining the sample size for adequate power to detect statistical significance is a crucial step at the design stage for high-throughput experiments. Even though a number of methods and tools are available for sample size calculation for microarray and RNA-seq in the context of differential expression (DE), this topic in the field of single-cell RNA sequencing is understudied. Moreover, the unique data characteristics present in scRNA-seq such as sparsity and heterogeneity increase the challenge. We propose POWSC, a simulation-based method, to provide power evaluation and sample size recommendation for single-cell RNA sequencing DE analysis. POWSC consists of a data simulator that creates realistic expression data, and a power assessor that provides a comprehensive evaluation and visualization of the power and sample size relationship.
    """

    bioc = "POWSC"

    version("1.16.0", commit="d9d3fce238e20816f44bd7ce6f0b5a4a688ef34f")
    version("1.10.0", commit="128061ccc7803855a0175d55a89ea4e2c296264c")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-mast", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
