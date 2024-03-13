# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSvaseq(RPackage):
    """The sva package contains functions for removing batch
    effects and other unwanted variation in high-throughput
    experiment. Specifically, the sva package contains functions
    for the identifying and building surrogate variables for
    high-dimensional data sets. Surrogate variables are covariates
    constructed directly from high-dimensional data (like gene
    expression/RNA sequencing/methylation/brain imaging data) that
    can be used in subsequent analyses to adjust for unknown,
    unmodeled, or latent sources of noise."""

    homepage = "https://github.com/zhangyuqing/sva-devel"
    git = "https://github.com/zhangyuqing/sva-devel"

    version("2020-09-24", commit="0a5550c6ff39ac61aa12306774b7d04eedf69ee3")

    depends_on("r-biocparallel", type=('build', 'run'))
    depends_on("r-genefilter", type=('build', 'run'))
    depends_on("r-matrixstats", type=('build', 'run'))
    depends_on("r-mgcv", type=('build', 'run'))
    depends_on("r-edger", type=('build', 'run'))
    depends_on("r-limma", type=('build', 'run'))
    depends_on("r-sva", type=('build', 'run'))
