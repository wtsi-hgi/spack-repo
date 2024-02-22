# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAiccmodavg(RPackage):
	"""Model Selection and Multimodel Inference Based on (Q)AIC(c)

	Functions to implement model selection and multimodel inference based on Akaike's information criterion (AIC) and the second-order AIC (AICc), as well as their quasi-likelihood counterparts (QAIC, QAICc) from various model object classes.  The package implements classic model averaging for a given parameter of interest or predicted values, as well as a shrinkage version of model averaging parameter estimates or effect sizes.  The package includes diagnostics and goodness-of-fit statistics for certain model types including those of 'unmarkedFit' classes estimating demographic parameters after accounting for imperfect detection probabilities.  Some functions also allow the creation of model selection tables for Bayesian models of the 'bugs', 'rjags', and 'jagsUI' classes.  Functions also implement model selection using BIC.  Objects following model selection and multimodel inference can be formatted to LaTeX using 'xtable' methods included in the package.
	"""
	
	cran = "AICcmodavg" 

	version("2.3-3", md5="aad20bc0b78d7e0100c9f6eac08a7789")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-unmarked", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
