# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstanarm(RPackage):
    """Bayesian Applied Regression Modeling via Stan
    
    Estimates previously compiled regression models using the 'rstan'
    package, which provides the R interface to the Stan C++ library for Bayesian
    estimation. Users specify models via the customary R syntax with a formula and
    data.frame plus some additional arguments for priors.
    """

    homepage = "https://cran.r-project.org/web/packages/rstanarm"
    
    cran = "rstanarm"

    # versions
    version("2.21.4", md5="5b7aabe08d62e45a8893c25d4f81a1ca")
    

    # dependencies
    depends_on("r-bayesplot@1.7.0:", type=('build', 'run'))
    depends_on("r-ggplot2@2.2.1:", type=('build', 'run'))
    depends_on("r-loo", type=('build', 'run'))
    depends_on("r-rstantools@2.1.0:", type=('build', 'run'))
    depends_on("r-shinystan@2.3.0:", type=('build', 'run'))
    depends_on("r-survival@2.40.1:", type=('build', 'run'))
    depends_on("r-rcpp-parallel@5.0.1:", type=('build', 'run'))
    
