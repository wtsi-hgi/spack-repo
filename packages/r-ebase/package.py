# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbase(RPackage):
	"""Estuarine Bayesian Single-Station Estimation Method for
Ecosystem Metabolism

	Estimate ecosystem metabolism in a Bayesian framework for
  individual water quality monitoring stations with continuous dissolved
  oxygen time series. A mass balance equation is used that provides
  estimates of parameters for gross primary production, respiration,
  and gas exchange. Methods adapted from Grace et al. (2015)
  <doi:10.1002/lom3.10011> and Wanninkhof (2014) <doi:10.4319/lom.2014.12.351>.
	"""
	
	homepage = "https://fawda123.github.io/EBASE/"
	cran = "EBASE" 

	version("1.0.0", md5="01adc979bb1a458fa90bfd6d3496db27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-r2jags@0.6.1:", type=("build", "run"))
	depends_on("r-rjags@4.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
