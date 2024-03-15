# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeostan(RPackage):
	"""Bayesian Spatial Analysis

	For Bayesian inference with spatial data, provides exploratory spatial analysis tools, multiple spatial model specifications, spatial model diagnostics, and special methods for inference with small area survey data (e.g., the America Community Survey (ACS)) and censored population health surveillance data. Models are pre-specified using the Stan programming language, a platform for Bayesian inference using Markov chain Monte Carlo (MCMC). References: Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>; Donegan (2021) <doi:10.31219/osf.io/3ey65>; Donegan (2022) <doi:10.21105/joss.04716>; Donegan, Chun and Hughes (2020) <doi:10.1016/j.spasta.2020.100450>; Donegan, Chun and Griffith (2021) <doi:10.3390/ijerph18136856>; Morris et al. (2019) <doi:10.1016/j.sste.2019.100301>.
	"""
	
	homepage = "https://connordonegan.github.io/geostan/"
	cran = "geostan" 

	version("0.5.4", md5="9458293582b0ecc33ec28e4b88e4550a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-spdep@1:", type=("build", "run"))
	depends_on("r-sf@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-signs", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
