# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcoxtime(RPackage):
	"""Penalized Cox Proportional Hazard Model for Time-Dependent
Covariates

	Fits penalized models for both time-independent and time-dependent survival data. It fully implements elastic net and uses proximal gradient descent to solve the optimization problem. The package is an implementation of Steve Cygu and Benjamin M. Bolker. (2021) <arXiv:2102.02297>.
	"""
	
	homepage = "https://github.com/CYGUBICKO/pcoxtime-pkg"
	cran = "pcoxtime" 

	version("1.0.4", md5="a715e49605f6ccb265f96c64a34a5251")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-permalgo", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
