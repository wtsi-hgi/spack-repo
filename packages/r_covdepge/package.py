# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovdepge(RPackage):
	"""Covariate Dependent Graph Estimation

	A covariate-dependent approach to Gaussian graphical modeling as described in Dasgupta et al. (2022). Employs a novel weighted pseudo-likelihood approach to model the conditional dependence structure of data as a continuous function of an extraneous covariate. The main function, covdepGE::covdepGE(), estimates a graphical representation of the conditional dependence structure via a block mean-field variational approximation, while several auxiliary functions (inclusionCurve(), matViz(), and plot.covdepGE()) are included for visualizing the resulting estimates. 
	"""
	
	homepage = "https://github.com/JacobHelwig/covdepGE"
	cran = "covdepGE" 

	version("1.0.1", md5="a96ad45af89b9c9ccf694f010532a0ac")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
