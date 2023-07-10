# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfactor(RPackage):
    """Computation of Bayes Factors for Common Designs
    
    A suite of functions for computing
    various Bayes factors for simple designs, including contingency tables,
    one- and two-sample designs, one-way designs, general ANOVA designs, and
    linear regression.
    """

    homepage = "https://cran.r-project.org/web/packages/BayesFactor"
    
    cran = "BayesFactor"

    # versions
    version("0.9.12-4.4", md5="a71faf9a86ddf787351494d563810b90")
    

    # dependencies
    depends_on("r-pbapply", type=('build', 'run'))
    depends_on("r-mvtnorm", type=('build', 'run'))
    depends_on("r-stringr", type=('build', 'run'))
    depends_on("r-graphics", type=('build', 'run'))
    depends_on("r-matrix-models", type=('build', 'run'))
    depends_on("r-rcpp", type=('build', 'run'))
    depends_on("r-hypergeo", type=('build', 'run'))
    
