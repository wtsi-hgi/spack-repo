# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZinbwave(RPackage):
    """Zero-Inflated Negative Binomial Model for RNA-Seq Data

    Implements a general and flexible zero-inflated negative binomial model that can be used to provide a low-dimensional representations of single-cell RNA-seq data. The model accounts for zero inflation (dropouts), over-dispersion, and the count nature of the data. The model also accounts for the difference in library sizes and optionally for batch effects and/or other covariates, avoiding the need for pre-normalize the data.
    """

    bioc = "zinbwave"

    version("1.30.0", commit="e7936299e04c25e0f478269d66183a924ed8445f")
    version("1.24.0", commit="84ae0eaf848045da5921d8a2d9555b7197dfc8af")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-softimpute", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
