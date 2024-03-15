# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesppdsurv(RPackage):
	"""Bayesian Power Prior Design for Survival Data

	Bayesian power/type I error calculation and model fitting using 
  the power prior and the normalized power prior for proportional hazards models
  with piecewise constant hazard. The Bayesian clinical trial design methodology is 
  described in Chen et al. (2011) <doi:10.1111/j.1541-0420.2011.01561.x>, 
  and Psioda and Ibrahim (2019) <doi:10.1093/biostatistics/kxy009>. 
  The proportional hazards model with piecewise constant hazard is detailed in 
  Ibrahim et al. (2001) <doi:10.1007/978-1-4757-3447-8>. 
	"""
	
	cran = "BayesPPDSurv" 

	version("1.0.2", md5="24725e571ff8669d1fdcfc9b816d9d64")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
