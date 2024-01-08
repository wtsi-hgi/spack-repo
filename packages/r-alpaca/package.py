# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAlpaca(RPackage):
    """Fit GLM's with High-Dimensional k-Way Fixed Effects
    
    Provides a routine to partial out factors with many levels during the optimization of the log-likelihood function of the corresponding generalized linear model (glm). The package is based on the algorithm described in Stammann (2018) <arXiv:1707.01815> and is restricted to glm's that are based on maximum likelihood estimation and nonlinear. It also offers an efficient algorithm to recover estimates of the fixed effects in a post-estimation routine and includes robust and multi-way clustered standard errors. Further the package provides analytical bias corrections for binary choice models derived by Fernandez-Val and Weidner (2016) <doi:10.1016/j.jeconom.2015.12.014> and Hinz, Stammann, and Wanner (2020) <arXiv:2004.12655>.
    """

    homepage = "https://cran.r-project.org/web/packages/alpaca"
    
    cran = "alpaca"

    version("0.3.4", md5="51c226ddd448efddee4d14a75b4c96c6")

    depends_on("r@3.1.0:", type=('build', 'run'))
    depends_on("r-formula", type=('build', 'run'))
    depends_on("r-mass", type=('build', 'run'))
    depends_on("r-rcpp", type=('build', 'run'))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    
