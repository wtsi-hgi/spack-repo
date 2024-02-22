# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantspec(RPackage):
	"""Quantile-Based Spectral Analysis of Time Series

	Methods to determine, smooth and plot quantile periodograms for
    univariate and multivariate time series. See Kley (2016) <doi:10.18637/jss.v070.i03>
    for a description and tutorial.
	"""
	
	homepage = "http://github.com/tobiaskley/quantspec"
	cran = "quantspec" 

	version("1.2-3", md5="bca4f4219c7820d233d286edb798e02e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
