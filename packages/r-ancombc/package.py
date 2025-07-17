# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAncombc(RPackage):
    """Microbiome differential abudance and correlation analyses with bias correction

    ANCOMBC is a package containing differential abundance (DA) and correlation analyses for microbiome data. Specifically, the package includes Analysis of Compositions of Microbiomes with Bias Correction 2 (ANCOM-BC2), Analysis of Compositions of Microbiomes with Bias Correction (ANCOM-BC), and Analysis of Composition of Microbiomes (ANCOM) for DA analysis, and Sparse Estimation of Correlations among Microbiomes (SECOM) for correlation analysis. Microbiome data are typically subject to two sources of biases: unequal sampling fractions (sample-specific biases) and differential sequencing efficiencies (taxon-specific biases). Methodologies included in the ANCOMBC package are designed to correct these biases and construct statistically consistent estimators.
    """

    homepage = "https://github.com/FrederickHuangLin/ANCOMBC"
    bioc = "ANCOMBC"

    version("2.10.1", commit="b1704fdaf1c8fd0ebbd0e290c3c502794c28a93c")
    version("2.4.0", commit="c60c1b0350589acd2694eb41283b2e3b6f0ab5d0")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-mia@1.6:", type=("build", "run"))
    depends_on("r-cvxr", type=("build", "run"))
    depends_on("r-desctools", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dorng", type=("build", "run"))
    depends_on("r-energy", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-lmertest", type=("build", "run"))
    depends_on("r-multcomp", type=("build", "run"))
    depends_on("r-nloptr", type=("build", "run"))
