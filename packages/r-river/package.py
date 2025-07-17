# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiver(RPackage):
    """R package for RIVER (RNA-Informed Variant Effect on Regulation)

    An implementation of a probabilistic modeling framework that jointly analyzes personal genome and transcriptome data to estimate the probability that a variant has regulatory impact in that individual. It is based on a generative model that assumes that genomic annotations, such as the location of a variant with respect to regulatory elements, determine the prior probability that variant is a functional regulatory variant, which is an unobserved variable. The functional regulatory variant status then influences whether nearby genes are likely to display outlier levels of gene expression in that person. See the RIVER website for more information, documentation and examples.
    """

    homepage = "https://github.com/ipw012/RIVER"
    bioc = "RIVER"

    version("1.32.0", commit="e278e1e2c4b0ffaf2bed05a92a880fd0df5463b1")
    version("1.26.0", commit="44ad7c632922288a0a7d3932ddb4921873a575b5")

    depends_on("r@3.3.2:", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
