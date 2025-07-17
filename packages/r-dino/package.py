# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDino(RPackage):
    """Normalization of Single-Cell mRNA Sequencing Data

    Dino normalizes single-cell, mRNA sequencing data to correct for technical variation, particularly sequencing depth, prior to downstream analysis. The approach produces a matrix of corrected expression for which the dependency between sequencing depth and the full distribution of normalized expression; many existing methods aim to remove only the dependency between sequencing depth and the mean of the normalized expression. This is particuarly useful in the context of highly sparse datasets such as those produced by 10X genomics and other uninque molecular identifier (UMI) based microfluidics protocols for which the depth-dependent proportion of zeros in the raw expression data can otherwise present a challenge.
    """

    homepage = "https://github.com/JBrownBiostat/Dino"
    bioc = "Dino"

    version("1.14.0", commit="aa7993ca237fbcc0218e076d64f51394047685b9")
    version("1.8.0", commit="6057572fd06608a3f54cf68a04629e6704110483")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
