# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsl(RPackage):
	"""Bayesian Synthetic Likelihood

	Bayesian synthetic likelihood (BSL, Price et al. (2018) <doi:10.1080/10618600.2017.1302882>)
    is an alternative to standard, non-parametric approximate Bayesian 
	computation (ABC). BSL assumes a multivariate normal distribution 
	for the summary statistic likelihood and it is suitable when the 
	distribution of the model summary statistics is sufficiently regular. 
	This package provides a Metropolis Hastings Markov chain Monte Carlo 
	implementation of four methods (BSL, uBSL, semiBSL and BSLmisspec) and two 
	shrinkage estimators (graphical lasso and Warton's estimator).
	uBSL (Price et al. (2018) <doi:10.1080/10618600.2017.1302882>) uses 
	an unbiased estimator to the normal density. A semi-parametric version 
	of BSL (semiBSL, An et al. (2018) <arXiv:1809.05800>) is more robust 
	to non-normal summary statistics. BSLmisspec (Frazier et al. 2019 
	<arXiv:1904.04551>) estimates the Gaussian synthetic likelihood whilst 
	acknowledging that there may be incompatibility between the model and the 
	observed summary statistic. Shrinkage estimation can help to decrease the
	number of model simulations when the dimension of the summary statistic is 
	high (e.g., BSLasso, An et al. (2019) <doi:10.1080/10618600.2018.1537928>). 
	Extensions to this package are planned. For a journal article describing how
	to use this package, see An et al. (2022) <doi:10.18637/jss.v101.i11>.
	"""
	
	cran = "BSL" 

	version("3.2.5", md5="b44def66477daa8971f2931f3be14c5a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-whitening", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
