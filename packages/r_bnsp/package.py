# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnsp(RPackage):
	"""Bayesian Non- And Semi-Parametric Model Fitting

	MCMC algorithms & processing functions for: 1. single response multiple regression, see Papageorgiou, G. (2018) <doi: 10.32614/RJ-2018-069>, 2. multivariate response multiple regression, with nonparametric models for the means, the variances and the correlation matrix, with variable selection, see Papageorgiou, G. and Marshall, B. C. (2020) <doi: 10.1080/10618600.2020.1739534>, 3. joint mean-covariance models for multivariate responses, see Papageorgiou, G. (2022) <doi: 10.1002/sim.9376>, and 4.Dirichlet process mixtures, see Papageorgiou, G. (2019) <doi: 10.1111/anzs.12273>.
	"""
	
	cran = "BNSP" 

	version("2.2.3", md5="31d6f8b867199b4faa3ab9a450e95c3b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-threejs", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-label-switching", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
