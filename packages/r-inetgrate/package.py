# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInetgrate(RPackage):
    """Integrates DNA methylation data with gene expression in a single gene network

    The iNETgrate package provides functions to build a correlation network in which nodes are genes. DNA methylation and gene expression data are integrated to define the connections between genes. This network is used to identify modules (clusters) of genes. The biological information in each of the resulting modules is represented by an eigengene. These biological signatures can be used as features e.g., for classification of patients into risk categories. The resulting biological signatures are very robust and give a holistic view of the underlying molecular changes.
    """

    bioc = "iNETgrate"

    version("1.6.0", commit="299831c72559623986945f77c71f6d43a938c00f")
    version("1.0.0", commit="d17858613410d05c52aa6e6122b18ca7f0504f5b")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocstyle@2.18.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicranges@1.24.1:", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-pigengene@1.19.26:", type=("build", "run"))
    depends_on("r-homo-sapiens", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-minfi", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rfast", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
