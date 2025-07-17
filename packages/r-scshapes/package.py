# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScshapes(RPackage):
    """A Statistical Framework for Modeling and Identifying Differential Distributions in Single-cell RNA-sequencing Data

    We present a novel statistical framework for identifying differential distributions in single-cell RNA-sequencing (scRNA-seq) data between treatment conditions by modeling gene expression read counts using generalized linear models (GLMs). We model each gene independently under each treatment condition using error distributions Poisson (P), Negative Binomial (NB), Zero-inflated Poisson (ZIP) and Zero-inflated Negative Binomial (ZINB) with log link function and model based normalization for differences in sequencing depth. Since all four distributions considered in our framework belong to the same family of distributions, we first perform a Kolmogorov-Smirnov (KS) test to select genes belonging to the family of ZINB distributions. Genes passing the KS test will be then modeled using GLMs. Model selection is done by calculating the Bayesian Information Criterion (BIC) and likelihood ratio test (LRT) statistic.
    """

    homepage = "https://github.com/Malindrie/scShapes"
    bioc = "scShapes"

    version("1.14.0", commit="13233ba8000a9b69b8bfd118c95e42f35eaf5a56")
    version("1.8.0", commit="430b1fe8583ab2bf3752e9d0e014a8e273b2fe38")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-pscl", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
    depends_on("r-dgof", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-emdbook", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
