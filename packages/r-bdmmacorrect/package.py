# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdmmacorrect(RPackage):
    """Meta-analysis for the metagenomic read counts data from different cohorts

    Metagenomic sequencing techniques enable quantitative analyses of the microbiome. However, combining the microbial data from these experiments is challenging due to the variations between experiments. The existing methods for correcting batch effects do not consider the interactions between variables—microbial taxa in microbial studies—and the overdispersion of the microbiome data. Therefore, they are not applicable to microbiome data. We develop a new method, Bayesian Dirichlet-multinomial regression meta-analysis (BDMMA), to simultaneously model the batch effects and detect the microbial taxa associated with phenotypes. BDMMA automatically models the dependence among microbial taxa and is robust to the high dimensionality of the microbiome and their association sparsity.
    """

    bioc = "BDMMAcorrect"

    version("1.20.0", commit="8c790c5f9d1e7b6286f228a12354737cd94f6ec6")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
