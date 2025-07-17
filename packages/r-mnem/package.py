# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnem(RPackage):
    """Mixture Nested Effects Models

    Mixture Nested Effects Models (mnem) is an extension of Nested Effects Models and allows for the analysis of single cell perturbation data provided by methods like Perturb-Seq (Dixit et al., 2016) or Crop-Seq (Datlinger et al., 2017). In those experiments each of many cells is perturbed by a knock-down of a specific gene, i.e. several cells are perturbed by a knock-down of gene A, several by a knock-down of gene B, ... and so forth. The observed read-out has to be multi-trait and in the case of the Perturb-/Crop-Seq gene are expression profiles for each cell. mnem uses a mixture model to simultaneously cluster the cell population into k clusters and and infer k networks causally linking the perturbed genes for each cluster. The mixture components are inferred via an expectation maximization algorithm.
    """

    homepage = "https://github.com/cbg-ethz/mnem/"
    bioc = "mnem"

    version("1.24.0", commit="c44ed4e408e16b096aaae08886be52c055e06a5c")
    version("1.18.0", commit="ad087eee616086a1b2a30610a23f2ff6a75f8840")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-flexclust", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-naturalsort", type=("build", "run"))
    depends_on("r-snowfall", type=("build", "run"))
    depends_on("r-tsne", type=("build", "run"))
    depends_on("r-linnorm", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-wesanderson", type=("build", "run"))
