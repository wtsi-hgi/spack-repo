# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStpm(RPackage):
	"""Stochastic Process Model for Analysis of Longitudinal and
Time-to-Event Outcomes

	Utilities to estimate parameters of the models with survival functions 
             induced by stochastic covariates. Miscellaneous functions for data preparation 
             and simulation are also provided. For more information, see: 
             (i)"Stochastic model for analysis of longitudinal data on aging and mortality" 
             by Yashin A. et al. (2007), 
             Mathematical Biosciences, 208(2), 538-551, <DOI:10.1016/j.mbs.2006.11.006>;
             (ii) "Health decline, aging and mortality: how are they related?" 
             by Yashin A. et al. (2007), 
             Biogerontology 8(3), 291(302), <DOI:10.1007/s10522-006-9073-3>.
	"""
	
	cran = "stpm" 

	version("1.7.12", md5="9171f22bbcbc15fb7e35ddf2d8da0860")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sas7bdat", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
