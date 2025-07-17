# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimentsubset(RPackage):
    """Manages subsets of data with Bioconductor Experiment objects

    Experiment objects such as the SummarizedExperiment or SingleCellExperiment are data containers for one or more matrix-like assays along with the associated row and column data. Often only a subset of the original data is needed for down-stream analysis. For example, filtering out poor quality samples will require excluding some columns before analysis. The ExperimentSubset object is a container to efficiently manage different subsets of the same data without having to make separate objects for each new subset.
    """

    bioc = "ExperimentSubset"

    version("1.18.1", commit="15c4278344605234bd6388fcb531603164294936")
    version("1.12.0", commit="a43cdbf3db54c4e9e17e322bfa42d1de999881ec")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
