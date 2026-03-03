# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLg(RPackage):
	"""Locally Gaussian Distributions: Estimation and Methods

	An implementation of locally Gaussian distributions. It provides methods for
    implementing locally Gaussian multivariate density estimation, conditional density 
    estimation, various independence tests for iid and time series data, a test for conditional 
    independence and a test for financial contagion.
	"""
	
	cran = "lg" 

	version("0.4.1", md5="bbb74445b1f1047ff3af2c3076446060")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-localgauss", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
