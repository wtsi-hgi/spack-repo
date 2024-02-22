# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppdist(RPackage):
	"""'Rcpp' Integration of Additional Probability Distributions

	The 'Rcpp' package provides a C++ library to make it easier
    to use C++ with R. R and 'Rcpp' provide functions for a variety of
    statistical distributions. Several R packages make functions
    available to R for additional statistical distributions. However,
    to access these functions from C++ code, a costly call to the R
    functions must be made. 'RcppDist' provides a header-only C++ library
    with functions for additional statistical distributions that can be
    called from C++ when writing code using 'Rcpp' or 'RcppArmadillo'.
    Functions are available that return a 'NumericVector' as well as
    doubles, and for multivariate or matrix distributions, 'Armadillo'
    vectors and matrices. 'RcppDist' provides functions for the following
    distributions: the four parameter beta distribution; the location-
    scale t distribution; the truncated normal distribution; the
    truncated t distribution; a truncated location-scale t distribution;
    the triangle distribution; the multivariate normal distribution*;
    the multivariate t distribution*; the Wishart distribution*; and
    the inverse Wishart distribution*. Distributions marked with an
    asterisk rely on 'RcppArmadillo'.
	"""
	
	homepage = "https://github.com/duckmayr/RcppDist"
	cran = "RcppDist" 

	version("0.1.1", md5="8a8b395463952d67e5a0c90d400b74c2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
