# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppnumerical(RPackage):
    """'Rcpp' Integration for Numerical Computing Libraries
    
    A collection of open source libraries for numerical computing
    (numerical integration, optimization, etc.) and their integration with
    'Rcpp'.
    """

    homepage = "https://cran.r-project.org/web/packages/RcppNumerical"
    
    cran = "RcppNumerical"

    # versions
    version("0.5-0", md5="4eeb679b306e9a464f2082e7ec7f2334")
    

    # dependencies
    depends_on("r-rcpp", type=('build', 'run'))
    
