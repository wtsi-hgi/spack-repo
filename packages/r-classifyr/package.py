# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassifyr(RPackage):
    """A framework for cross-validated classification problems, with applications to differential variability and differential distribution testing

    The software formalises a framework for classification and survival model evaluation in R. There are four stages; Data transformation, feature selection, model training, and prediction. The requirements of variable types and variable order are fixed, but specialised variables for functions can also be provided. The framework is wrapped in a driver loop that reproducibly carries out a number of cross-validation schemes. Functions for differential mean, differential variability, and differential distribution are included. Additional functions may be developed by the user, by creating an interface to the framework.
    """

    homepage = "https://sydneybiox.github.io/ClassifyR/"
    bioc = "ClassifyR"

    version("3.12.2", commit="c21a3ca326b353fed83df9a2014d411fa299212e")
    version("3.6.5", commit="8533331fcc3df644c9ee183bd9b9c58deaec6c0d")
    version("3.6.3", md5="d7ab30daf86208976868d3f9b82b67de")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-generics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-ranger", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggupset", type=("build", "run"))
    depends_on("r-dcanr", type=("build", "run"))
