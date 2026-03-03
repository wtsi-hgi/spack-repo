# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmr(RPackage):
	"""A Stable Isotope Mixing Model

	Fits Stable Isotope Mixing Models (SIMMs) and is meant as a longer term replacement to the previous widely-used package SIAR. SIMMs are used to infer dietary proportions of organisms consuming various food sources from observations on the stable isotope values taken from the organisms' tissue samples. However SIMMs can also be used in other scenarios, such as in sediment mixing or the composition of fatty acids. The main functions are simmr_load() and simmr_mcmc(). The two vignettes contain a quick start and a full listing of all the features. The methods used are detailed in the papers Parnell et al 2010 <doi:10.1371/journal.pone.0009672>, and Parnell et al 2013 <doi:10.1002/env.2221>.
	"""
	
	homepage = "https://github.com/andrewcparnell/simmr"
	cran = "simmr" 

	version("0.5.1.216", md5="e9809923b63829cee087fee526526b85")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
