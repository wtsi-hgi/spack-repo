# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsnbayes(RPackage):
	"""Bayesian Spatio-Temporal Analysis in Stream Networks

	Fits Bayesian spatio-temporal models and makes predictions on stream networks using the approach by Santos-Fernandez, Edgar, et al. (2022)."Bayesian spatio-temporal models for stream networks". <arXiv:2103.03538>. In these models, spatial dependence is captured using stream distance and flow connectivity, while temporal autocorrelation is modelled using vector autoregression methods. 
	"""
	
	homepage = "https://github.com/EdgarSantos-Fernandez/SSNbayes"
	cran = "SSNbayes" 

	version("0.0.3", md5="83416ee96882dd56e56a14b7cf72d274")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ssn2", type=("build", "run"))
