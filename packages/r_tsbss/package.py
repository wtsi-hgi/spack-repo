# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsbss(RPackage):
	"""Blind Source Separation and Supervised Dimension Reduction for
Time Series

	Different estimators are provided to solve the blind source separation problem for multivariate time series with stochastic volatility and supervised dimension reduction problem for multivariate time series. Different functions based on AMUSE and SOBI are also provided for estimating the dimension of the white noise subspace. The package is fully described in Nordhausen, Matilainen, Miettinen, Virta and Taskinen (2021) <doi:10.18637/jss.v098.i15>.
	"""
	
	cran = "tsBSS" 

	version("1.0.0", md5="f8e24102d91950cb05a378e096143691")

	depends_on("r-ictest@0.3.2:", type=("build", "run"))
	depends_on("r-jade@2.0.2:", type=("build", "run"))
	depends_on("r-bssprep", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
