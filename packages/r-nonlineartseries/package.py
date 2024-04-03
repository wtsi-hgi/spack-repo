# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonlineartseries(RPackage):
	"""Nonlinear Time Series Analysis

	Functions for nonlinear time series analysis. This package permits
    the computation of the  most-used nonlinear statistics/algorithms
    including generalized correlation dimension, information dimension,
    largest Lyapunov exponent, sample entropy and Recurrence
    Quantification Analysis (RQA), among others. Basic routines
    for surrogate data testing are also included. Part of this work
    was based on the  book "Nonlinear time series analysis" by
    Holger Kantz and Thomas Schreiber (ISBN: 9780521529020).
	"""
	
	homepage = "https://github.com/constantino-garcia/nonlinearTseries"
	cran = "nonlinearTseries" 

	version("0.3.0", md5="da3c2ba97df1bd38d721603193fad235")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
