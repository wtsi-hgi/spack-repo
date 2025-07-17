# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScds(RPackage):
    """In-Silico Annotation of Doublets for Single Cell RNA Sequencing Data

    In single cell RNA sequencing (scRNA-seq) data combinations of cells are sometimes considered a single cell (doublets). The scds package provides methods to annotate doublets in scRNA-seq data computationally.
    """

    bioc = "scds"

    version("1.24.0", commit="41355d9ea426a3c5d1bc20eb516fb0d915fd7bc2")
    version("1.18.0", commit="dff0c08768ad7884239dfcca4570b45aacce80e9")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-xgboost", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
