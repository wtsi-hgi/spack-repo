# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoconots(RPackage):
	"""Convolution-Closed Models for Count Time Series

	Useful tools for fitting, validating, and forecasting of practical convolution-closed time series models for low counts are provided. Marginal distributions of the data can be modeled via Poisson and Generalized Poisson innovations. Regression effects can be modelled via time varying innovation rates. The models are described in Jung and Tremayne (2011) <doi:10.1111/j.1467-9892.2010.00697.x> and the model assessment tools are presented in Czado et al. (2009) <doi:10.1111/j.1541-0420.2009.01191.x>, Gneiting and Raftery (2007) <doi:10.1198/016214506000001437> and, Tsay (1992) <doi:10.2307/2347612>.
	"""
	
	cran = "coconots" 

	version("1.1.3", md5="b28a6c7a991a40753a7fa6bb9d27c753")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-hmmpa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
	depends_on("r-stanheaders@2.21:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
