# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsgsca(RPackage):
    """Association Studies for multiple SNPs and multiple traits using Generalized Structured Equation Models

    The package provides tools to model and test the association between multiple genotypes and multiple traits, taking into account the prior biological knowledge. Genes, and clinical pathways are incorporated in the model as latent variables. The method is based on Generalized Structured Component Analysis (GSCA).
    """

    bioc = "ASGSCA"

    version("1.42.0", commit="3220f6ae1adef3504e7a0490549f31f2e4bf45d2")
    version("1.36.0", commit="e11a7118ad56777d0bdbb4dc450903137fe39a26")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
