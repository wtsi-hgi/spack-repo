# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbmp(RPackage):
    """Variational Bayesian Multinomial Probit Regression

    Variational Bayesian Multinomial Probit Regression with Gaussian Process Priors. It estimates class membership posterior probability employing variational and sparse approximation to the full posterior. This software also incorporates feature weighting by means of Automatic Relevance Determination.
    """

    homepage = "http://bioinformatics.oxfordjournals.org/cgi/content/short/btm535v1"
    bioc = "vbmp"

    version("1.76.0", commit="e4596368f6f47bcf3f5e74ccc42af51e1080d188")
    version("1.70.0", commit="afca3e6a5aa86ec5531ff5cdcf61336d8f7fb3d6")

    depends_on("r@2.10:", type=("build", "run"))
