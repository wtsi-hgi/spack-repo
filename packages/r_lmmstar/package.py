# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmmstar(RPackage):
	"""Repeated Measurement Models for Discrete Times

	Companion R package for the course "Statistical analysis of correlated and repeated measurements for health science researchers"
	     taught by the section of Biostatistics of the University of Copenhagen.
	     It implements linear mixed models where the model for the variance-covariance of the residuals is specified via patterns (compound symmetry, toeplitz, unstructured, ...).
	     Statistical inference for mean, variance, and correlation parameters is performed based on the observed information and a Satterthwaite approximation of the degrees of freedom.
	     Normalized residuals are provided to assess model misspecification.
	     Statistical inference can be performed for arbitrary linear or non-linear combination(s) of model coefficients.
	     Predictions can be computed conditional to covariates only or also to outcome values. 
	"""
	
	homepage = "https://github.com/bozenne/LMMstar"
	cran = "LMMstar" 

	version("1.0.1", md5="ac64fc7024afee5b87c5d5ae313c9491")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
