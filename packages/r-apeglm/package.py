# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApeglm(RPackage):
    """apeglm provides Bayesian shrinkage estimators for effect sizes for a variety of GLM models, using approximation of the posterior for individual coefficients."""

    url = "https://bioconductor.org/packages/release/bioc/src/contrib/apeglm_1.22.1.tar.gz"
    bioc = "apeglm"

    version("1.24.0", sha256="a4ff49d510b9021328c9f56bfbd3af55905c8a2c53ccdaf3986ef004ebf74932")

    depends_on("r-biocinstaller", type=("build", "run"))
    depends_on("r-emdbook", type=('build', 'run'))
    depends_on("r-summarizedexperiment", type=('build', 'run'))
    depends_on("r-genomicranges", type=('build', 'run'))
    depends_on("r-rcpp", type=('build', 'run'))
    depends_on("r-rcppeigen", type=('build', 'run'))
    depends_on("r-rcppnumerical", type=('build', 'run'))

