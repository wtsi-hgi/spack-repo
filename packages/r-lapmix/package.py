# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLapmix(RPackage):
    """Laplace Mixture Model in Microarray Experiments

    Laplace mixture modelling of microarray experiments. A hierarchical Bayesian approach is used, and the hyperparameters are estimated using empirical Bayes. The main purpose is to identify differentially expressed genes.
    """

    homepage = "http://www.r-project.org"
    bioc = "lapmix"

    version("1.74.0", commit="58eb049904607cf01e2dde484e0ae37bc333314b")
    version("1.68.0", commit="3104a129a4a3d770d5f75581a47681b78396158b")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
