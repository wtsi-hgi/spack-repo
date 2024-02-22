# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpr(RPackage):
	"""Fitting Bayesian Poisson Regression

	Posterior sampling and inference for Bayesian Poisson regression models. The model specification makes use of Gaussian (or conditionally Gaussian) prior distributions on the regression coefficients. Details on the algorithm are found in D'Angelo and Canale (2023) <doi:10.1080/10618600.2022.2123337>.
	"""
	
	cran = "bpr" 

	version("1.0.7", md5="14aa3334a5857c78029575ff220aecce")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
