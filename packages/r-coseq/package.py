# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoseq(RPackage):
    """Co-Expression Analysis of Sequencing Data

    Co-expression analysis for expression profiles arising from high-throughput sequencing data. Feature (e.g., gene) profiles are clustered using adapted transformations and mixture models or a K-means algorithm, and model selection criteria (to choose an appropriate number of clusters) are provided.
    """

    bioc = "coseq"

    version("1.32.1", commit="e039f79be3260a457c4716639f74d749f8f007dd")
    version("1.26.0", commit="985d20a051646174a8be7cd900de200a1c6ee0cb")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-capushe", type=("build", "run"))
    depends_on("r-rmixmod", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-htsfilter", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-htscluster", type=("build", "run"))
    depends_on("r-compositions", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
